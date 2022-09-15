from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from .forms import calendarform, offsetForm
from .models import *
from django.http import HttpResponse
from django.db.models import F
from datetime import datetime


def srecalendarapp(request):
    offsetdata = offset.objects.all().values('offset_id','sre','offset_start','offset_end','offset_used','offset_expiring',name = F('sre__first_name'))
    for j in offsetdata:

        j['remaing'] = j['offset_end'] - j['offset_start']
        startdate = datetime.strptime(str(j['offset_start'])[:19], '%Y-%m-%d %H:%M:%S')
        enddate = datetime.strptime(str(j['offset_end'])[:19], '%Y-%m-%d %H:%M:%S')

        timedelta = enddate - startdate
        timedelta = timedelta.total_seconds() / 3600
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
                fetchsre = sre.objects.get(sre_id = Sre)
                off_form = offset(sre=fetchsre,offset_start=offset_start,offset_end=offset_end)                      
                off_form.save()
                return redirect('srecalendarapp')

            else:
                status = True
                checkalready.offset_start = offset_start
                checkalready.offset_end = offset_end
                checkalready.save()
                if 'statusmessage' in request.POST:
                    return redirect('srecalendarapp')


                context = {'cal_form' : calendarform, "calendar": all_events , "list_type": list_type.objects.values("name") , 'off_form' : offsetForm,"offsetdata":offsetdata,'sredata':sredata,"status":status,"message":"User already exists"}
                
                return render(request, "srecalendarapp.html", context)

        
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
            timedelta = enddate - startdate
            timedelta = timedelta.total_seconds() / 3600
            fetchoffset = offset.objects.filter(sre =Sre ).first()
            if fetchoffset:
                

                ##edit work
                if calenderid:
                    fetchdata = calendar_list.objects.get(calendar_id = calenderid)
                    fetchdata.start_date = start_date
                    fetchdata.end_date = end_date
                    fetchdata.description = description
                    fetchdata.type = typeobj
                    fetchdata.save()
                    return redirect('srecalendarapp')


                obj  = calendar_list(type = typeobj,start_date = start_date,end_date = end_date,description = description,sre = fetchsre)
                obj.save()

                ##cut hours
                
                fetchoffset.offset_used = fetchoffset.offset_used + timedelta
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