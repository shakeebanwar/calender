from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .forms import calendarform, offsetForm
from .models import *
from django.http import HttpResponse
from django.db.models import F
from datetime import datetime
import srecalendarapp.usable as uf


def srecalendarapp(request):
    offsetdata = offset.objects.all().values('offset_id','sre','offset_start','offset_end','offset_used','offset_expiring',name = F('sre__first_name'))
    for j in offsetdata:
        

        
        todayobj = datetime.strptime(str(datetime.now() )[:19], '%Y-%m-%d %H:%M:%S')
        expireCal = datetime.strptime(str(j['offset_expiring'])[:19], '%Y-%m-%d %H:%M:%S')
        startdate = datetime.strptime(str(j['offset_start'])[:19], '%Y-%m-%d %H:%M:%S')
        enddate = datetime.strptime(str(j['offset_end'])[:19], '%Y-%m-%d %H:%M:%S')

        timedelta = enddate - startdate
        timedelta = timedelta.total_seconds() / 3600
        j['remaing'] = expireCal - todayobj
        j['hours'] = int(timedelta)
        j['offset_used'] = int(j['offset_used'])
        j['balance'] = int(timedelta) - int(j['offset_used'])
        
        

  

    all_events = calendar_list.objects.all()
    sredata = sre.objects.all()
    typedata = list_type.objects.all()


    if request.POST:
        if "off-save" in request.POST:
            Sre = request.POST['sre']
            offset_start = request.POST['offset_start']
            offset_end = request.POST['offset_end']
            ## check  if not exist
            checkalready = offset.objects.filter(sre = Sre).first()
            if not checkalready:
                startdate = datetime.strptime(str(offset_start)[:19], '%Y-%m-%dT%H:%M')
                enddate = datetime.strptime(str(offset_end)[:19], '%Y-%m-%dT%H:%M')
                timedeltas = enddate - startdate
                expiration = timedeltas.total_seconds() / 3600
                hours = int(expiration)
                offset_used = 0
                balance = int(expiration) - int(offset_used)
                expirationDays = uf.expireCalculate()
                
                fetchsre = sre.objects.get(sre_id = Sre)
                off_form = offset(sre=fetchsre,offset_start=offset_start,offset_end=offset_end,offset_total = hours , offset_expiring = expirationDays,offset_bal = balance)                      
                off_form.save()
                return redirect('srecalendarapp')

            else:
                print("else is hitting")
                # return HttpResponse("OK")
                               
                timedelta = enddate - startdate
                expiration = timedelta.total_seconds() / 3600
                hours = int(expiration)
                balance = int(expiration) - int(checkalready.offset_used)

                status = False
                checkalready.offset_start = offset_start
                checkalready.offset_end = offset_end
                checkalready.offset_total = hours
                # checkalready.offset_expiring = timedelta
                checkalready.offset_bal = balance
                checkalready.save()
                # return HttpResponse("OK")
                if 'statusmessage' in request.POST:
                    return redirect('srecalendarapp')

                return redirect('srecalendarapp')
                # context = {'cal_form' : calendarform, "calendar": all_events , "list_type": list_type.objects.values("name") , 'off_form' : offsetForm,"offsetdata":offsetdata,'sredata':sredata,"status":status,"message":"User already exists"}
                
                # return render(request, "srecalendarapp.html", context)

        
        else:
            calenderid = request.POST.get('calenderidvalue',False)
            typedata = request.POST['type']
            start_date = request.POST['start_date']
            end_date = request.POST['end_date']
            Sre = request.POST['sre']
            description = request.POST['description']
            fetchsre = sre.objects.get(sre_id = Sre)
            typeobj = list_type.objects.get(type_id = typedata)

            startdate = datetime.strptime(str(start_date)[:19], '%Y-%m-%dT%H:%M')
            enddate = datetime.strptime(str(end_date)[:19], '%Y-%m-%dT%H:%M')
            expiration = enddate - startdate
            timedelta = expiration.total_seconds() / 3600
            fetchoffset = offset.objects.filter(sre =Sre ).first()

            if typeobj.name != "Offset" or fetchoffset:
                

                ##edit work
                if calenderid:
                    fetchdata = calendar_list.objects.get(calendar_id = calenderid)
                    ##Extra hourse subtract
                    editstartdate = datetime.strptime(str(fetchdata.start_date)[:19], '%Y-%m-%d %H:%M:%S')
                    editenddate = datetime.strptime(str(fetchdata.end_date)[:19], '%Y-%m-%d %H:%M:%S')
                    editexpiration = editenddate - editstartdate
                    edittimedelta = editexpiration.total_seconds() / 3600



                    fetchdata.start_date = start_date
                    fetchdata.end_date = end_date
                    fetchdata.description = description
                    fetchdata.type = typeobj
                    fetchdata.offset_expiring = expiration
                    fetchdata.offset_total = timedelta
                    fetchoffset.offset_used = timedelta + edittimedelta -edittimedelta
                    fetchoffset.offset_bal = fetchoffset.offset_bal - timedelta
                    fetchdata.save()
                    fetchoffset.save()
                    
                    return redirect('srecalendarapp')


                obj  = calendar_list(type = typeobj,start_date = start_date,end_date = end_date,description = description,sre = fetchsre)
                obj.save()

                ##cut hours
                if typeobj.name == "Offset":
                    fetchoffset.offset_used = fetchoffset.offset_used + timedelta
                    fetchoffset.offset_bal = fetchoffset.offset_bal - timedelta
                    fetchoffset.save()
                return redirect('srecalendarapp')

            else:
                context = {'cal_form' : calendarform, "calendar": all_events , "list_type": list_type.objects.values("name") , 'off_form' : offsetForm,"offsetdata":offsetdata,'sredata':sredata,"status":True,"message":"First Enter UserOffset"}
                
                return render(request, "srecalendarapp.html", context)


            




    context = {'cal_form' : calendarform, "calendar": all_events , "list_type": list_type.objects.values("name") , 'off_form' : offsetForm,"offsetdata":offsetdata,'sredata':sredata,"typedata":typedata}
    return render(request, "srecalendarapp.html", context)




def deleteoffset(requet,id):
    try:
        offset.objects.get(offset_id = id).delete()
        return redirect('srecalendarapp')

    except:
        return redirect('srecalendarapp')



def deletecalender(requet,id):
    try:
        calendar_list.objects.get(calendar_id = id).delete()
        return redirect('srecalendarapp')

    except:
        return redirect('srecalendarapp')
