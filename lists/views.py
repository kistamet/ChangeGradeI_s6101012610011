from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GPA,Datagrade
#หน้า Gradecalculator
def home_page(request):
    return render(request, 'home.html')

#หน้า HomePage แรก
def register(request):
    count = User.objects.count()
    #นับจำนวณ User
    return render(request, 'index.html', {
        'count': count
    })
#หน้า signup
#ใช้ django signup from
def signup(request):
    #ถ้ากรอกข้อมูลตามเงื่อนไข from django ได้ถูกต้อง
    #จะทำการ save ข้อมูล
    #และ login อัตโนมัติ
    if request.method == 'POST':
        #เช็ค request
        form = UserCreationForm(request.POST)
        # เช็คความถูกต้องของ form
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user.save()
            user = authenticate(username=username, password=raw_password)#ตรวจสอบความถูกต้องของข้อมูล username password
            login(request, user)
            return redirect('home')
    # ถ้าไม่ถูกจะ return หน้า signup และมีข้อบอกว่าทำไมถึงกรอกไม่ถูกเงื่อนไข
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })
#หน้า Gradecalculator และปุ่มกด Save
def calGrade(request):
    if request.method == 'POST':
        # เช็ค input
        if request.POST.get('subjectTerm') == "0":
            message = 'Please select term before saving grade'
            return render(request, 'home.html', {'message': message})
        not_input = "Plese check your infromation before saving."
        checkinput = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject1Grade')) + \
                     float(request.POST.get('subject2Unit')) + float(request.POST.get('subject2Grade')) + \
                     float(request.POST.get('subject3Unit')) + float(request.POST.get('subject3Grade')) + \
                     float(request.POST.get('subject4Unit')) + float(request.POST.get('subject4Grade')) + \
                     float(request.POST.get('subject5Unit')) + float(request.POST.get('subject5Grade')) + \
                     float(request.POST.get('subject6Unit')) + float(request.POST.get('subject6Grade')) + \
                     float(request.POST.get('subject7Unit')) + float(request.POST.get('subject7Grade')) + \
                     float(request.POST.get('subject8Unit')) + float(request.POST.get('subject8Grade')) + \
                     float(request.POST.get('subject9Unit')) + float(request.POST.get('subject9Grade'))
        # ไม่ได้กรอกข้อมูลจะแสดง "Plese check your infromation before saving."
        if checkinput == 0.0:
            return render(request, 'home.html', {'notinput': not_input})
        # ผลคูณของ Unit ตัวที่ 1 กับ Grade ตัวที่ 1 ถึง ผลคูณของ Unit ตัวที่ 9 กับ Grade ตัวที่ 9
        sub1 = float(request.POST.get('subject1Unit')) * float(request.POST.get('subject1Grade'))
        sub2 = float(request.POST.get('subject2Unit')) * float(request.POST.get('subject2Grade'))
        sub3 = float(request.POST.get('subject3Unit')) * float(request.POST.get('subject3Grade'))
        sub4 = float(request.POST.get('subject4Unit')) * float(request.POST.get('subject4Grade'))
        sub5 = float(request.POST.get('subject5Unit')) * float(request.POST.get('subject5Grade'))
        sub6 = float(request.POST.get('subject6Unit')) * float(request.POST.get('subject6Grade'))
        sub7 = float(request.POST.get('subject7Unit')) * float(request.POST.get('subject7Grade'))
        sub8 = float(request.POST.get('subject8Unit')) * float(request.POST.get('subject8Grade'))
        sub9 = float(request.POST.get('subject9Unit')) * float(request.POST.get('subject9Grade'))
        # ผลรวมของ unit ทั้งหมด
        sumunit = float(request.POST.get('subject1Unit')) + float(request.POST.get('subject2Unit')) + float(
            request.POST.get('subject3Unit')) + float(request.POST.get('subject4Unit')) + float(
            request.POST.get('subject5Unit')) + float(request.POST.get('subject6Unit')) + float(
            request.POST.get('subject7Unit')) + float(request.POST.get('subject8Unit')) + float(
            request.POST.get('subject9Unit')
        )
        # ผลรวมของ Unit ตัวที่ 1 กับ Grade ตัวที่ 1 ถึง Unit ตัวที่ 9 กับ Grade ตัวที่ 9
        sumsub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6 + sub7 + sub8 + sub9
        # นำผลรวมของ Unit ตัวที่ 1 กับ Grade ตัวที่ 1 ถึง Unit ตัวที่ 9 กับ Grade ตัวที่ 9 มาหาร ผลรวมของ unit ทั้งหมด
        res = '%.2f' %(sumsub / sumunit)
        #รับค่าจาก User และบันทึกค่าลง Batabase
        if len(Datagrade.objects.all()) != 0:
            # Update ค่า
            for i in Datagrade.objects.all():
                #ลบค่าของ subject unit Grade term user ที่เคยบันทีกไว้
                if request.user == i.user and i.term == request.POST.get('subjectTerm'):
                    Datagrade.objects.filter(pk=i.id).delete()
            for item in GPA.objects.all():
                #ลบค่าของ GPA ที่เคยบันทีกไว้
                if request.user == item.user and item.termgpa == request.POST.get('subjectTerm'):
                    GPA.objects.filter(pk=item.id).delete()
        # ทำการสร้าง subject unit Grade term user จาก input ของ User
        Datagrade.objects.create(subject=request.POST['subject1name'],unit=request.POST['subject1Unit'],
                                 Grade=request.POST['subject1Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user,GPA=res)
        Datagrade.objects.create(subject=request.POST['subject2name'], unit=request.POST['subject2Unit'],
                                 Grade=request.POST['subject2Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject3name'], unit=request.POST['subject3Unit'],
                                 Grade=request.POST['subject3Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject4name'], unit=request.POST['subject4Unit'],
                                 Grade=request.POST['subject4Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject5name'], unit=request.POST['subject5Unit'],
                                 Grade=request.POST['subject5Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject6name'], unit=request.POST['subject6Unit'],
                                 Grade=request.POST['subject6Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject7name'], unit=request.POST['subject7Unit'],
                                 Grade=request.POST['subject7Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject8name'], unit=request.POST['subject8Unit'],
                                 Grade=request.POST['subject8Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        Datagrade.objects.create(subject=request.POST['subject9name'], unit=request.POST['subject9Unit'],
                                 Grade=request.POST['subject9Grade'], term=request.POST.get('subjectTerm'),
                                 user=request.user)
        #สร้าง GPA user termgpa GPAX
        GPA.objects.create(GPA=res,user=request.user,termgpa=request.POST.get('subjectTerm'),GPAX="0")
        return render(request, 'home.html', {'result': res})
def flow(request):
    Result = ''
    subjects = str(request.POST.get('searchFlow',''))
    # search แต่ละวิชา
    if 'searchSubject' in request.POST :
        #1ProFund
        if subjects == "Programming Fundamental" :
            Result = """Semister2 : Algorithms and Data Structures <br />
            Semister5 : Operating Systems"""
        #2MathI
        elif subjects == "Engineering Mathematics I" :
            Result = """Semister2 : Math II <br />
            Semister3 : Statistics for Computer Engineer"""
        #3ComExplo
        elif subjects == "Computer Engineering Exploration" :
            Result = "The subject hasn't other subjects to connect the flow"
        #4PhysicsI
        elif subjects == "Physics I" :
            Result = "Semister2 : Physics II"
        #5PhyLabI
        elif subjects == "Physics Laboratory I" :
            Result = "The subject hasn't other subjects to connect the flow"
        #6EnglishI
        elif subjects == "Language Elective Course I" :
            Result = "Language Elective Course II"
        #7TableTennis
        elif subjects == "Physical Education Elective Course I" :
            Result = "Physical Education Elective Course II"
        #8ManSo
        elif subjects == "Social Sciences Elective Course" :
            Result = "The subject hasn't other subjects to connect the flow"
        #9Intro
        elif subjects == "Introduction to Engineer" :
            Result = "The subject hasn't other subjects to connect the flow"
        #10Circuit
        elif subjects == "Electric Circuit Theory" :
            Result = "Semister4 : Analog and Digital Electronics"
        #11CircuitLab
        elif subjects == "Electric Circuit Lab" :
            Result = "The subject hasn't other subjects to connect the flow"
        #12Algo
        elif subjects == "Algorithms and Data Structure" :
            Result = """Semister3 : Software Development Practice I <br />
            Semister5 : Computer Organization <br />
            Semister6 : Database Systems"""
        #13Work Ethics
        elif subjects == "Work Ethics" :
            Result = "The subject hasn't other subjects to connect the flow"
        #14MathII
        elif subjects == "Engineering Mathematics II" :
            Result = """Semister3 : Discrete Mathematics <br />
            Semister3 : Introduction to Signals and System"""
        #15PhysicsII
        elif subjects == "Physics II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #16PhyLab2
        elif subjects == "Physics Laboratory II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #17EnglishII
        elif subjects == "Language Elective Course II" :
            Result = "Language Elective Course III"
        #18Basketball
        elif subjects == "Physical Education Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #19Stat
        elif subjects == "Statistics for Computer Engineer" :
            Result = "The subject hasn't other subjects to connect the flow"
        #20Signal
        elif subjects == "Introduction to Signals and System" :
            Result = "The subject hasn't other subjects to connect the flow"
        #21Digital
        elif subjects == "Logic Design of Digital System" :
            Result = """Semister3 : Digital System Design Laboratory <br />
            Semister4 : Computer Organization"""
        #22DigiLab
        elif subjects == "Digital System Design Laboratory" :
            Result = "The subject hasn't other subjects to connect the flow"
        #23SoftwareI
        elif subjects == "Software Development Practice I" :
            Result = "Semister4 : Software Development Practice II"
        #24Discrete Math
        elif subjects == "Discrete Mathematics" :
            Result = "Semister6 : Database Systems"
        #25PhyLife
        elif subjects == "Science and Maths Elective I" :
            Result = "Science and Maths Elective II"
        #26SoftwareII
        elif subjects == "Software Development Practice II" :
            Result = "Semister5 : Software Engineering"
        #27NetworkI
        elif subjects == "Computer Networks I" :
            Result = "Semister5 : Computer Networks II"
        #28ComOr
        elif subjects == "Computer Organization" :
            Result = "Semister5 : Embedded System Design"
        #29Ubi
        elif subjects == "Ubiquitous Computing" :
            Result = "The subject hasn't other subjects to connect the flow"
        #30Analog
        elif subjects == "Analog and Digital Electronics" :
            Result = "Semister5 : Analog and Digital Electronics Lab"
        #31GenMath
        elif subjects == "Science and Maths Elective II" :
            Result = "Science and Maths Elective III"
        #32SoftEng
        elif subjects == "Software Engineering" :
            Result = "The subject hasn't other subjects to connect the flow"
        #33NetworkII
        elif subjects == "Computer Networks II" :
            Result = "Semister6 : Computer Networks Lab"
        #34OS
        elif subjects == "Operating Systems" :
            Result = "The subject hasn't other subjects to connect the flow"
        #35Embedded
        elif subjects == "Embedded System Design" :
            Result = "Semister6 : Embedded System Design Laboratory"
        #36AnalogLab
        elif subjects == "Analog and Digital Electronics Lab" :
            Result = "The subject hasn't other subjects to connect the flow"
        #37Language Elective III
        elif subjects == "Language Elective Course III" :
            Result = "Language Elective Course IV"
        #38Database
        elif subjects == "Database Systems" :
            Result = "The subject hasn't other subjects to connect the flow"
        #39NetworkLab
        elif subjects == "Computer Networks Lab" :
            Result = "The subject hasn't other subjects to connect the flow"
        #40EmbeddedLab
        elif subjects == "Embedded System Design Laboratory" :
            Result = "The subject hasn't other subjects to connect the flow"
        #41Language Elective IV
        elif subjects == "Language Elective Course IV" :
            Result = "The subject hasn't other subjects to connect the flow"
        #42Computer Eng. Elective Course I
        elif subjects == "Computer Eng. Elective Course I" :
            Result = "Computer Eng. Elective Course II"
        #43Computer Eng. Elective Course II
        elif subjects == "Computer Eng. Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #44Humanities Elective Course I
        elif subjects == "Humanities Elective Course I" :
            Result = "Humanities Elective Course II"
        #45ProjectI
        elif subjects == "Project I" :
            Result = "Semister8 : Project II"
        #46Free Elective Course I
        elif subjects == "Free Elective Course I" :
            Result = "Free Elective Course I"
        #47Humanities Elective Course II
        elif subjects == "Humanities Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #48Computer Eng. Elective Course III
        elif subjects == "Computer Eng. Elective Course III" :
            Result = "Computer Eng. Elective Course IV"
        #49Computer Eng. Elective Course IV
        elif subjects == "Computer Eng. Elective Course IV" :
            Result = "The subject hasn't other subjects to connect the flow"
        #50ProjectII
        elif subjects == "Project II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #51Computer Eng. Seminar
        elif subjects == "Computer Eng. Seminar" :
            Result = "The subject hasn't other subjects to connect the flow"
        #52Free Elective Course II
        elif subjects == "Free Elective Course II" :
            Result = "The subject hasn't other subjects to connect the flow"
        #53Science and Maths Elective III
        elif subjects == "Science and Maths Elective III" :
            Result = "The subject hasn't other subjects to connect the flow"
        #Other
        else :
            Result = "The subject isn't in the flow"
    
    return render(request, 'flow.html',{'subjects':subjects, 'Result':Result})
def listOfSubject(request) :
    # ดูวิชาแต่ละเทอม
    listSemister1 = """ Programming Fundamental<br />
            Engineering Mathematics I<br />
            Computer Engineering Exploration<br />
            Physics I<br />
            Physics Laboratory I<br />
            Language Elective Course I<br />
            Physical Education Elective Course I<br />
            Social Sciences Elective Course<br />
            Introduction to Engineer<br />"""

    listSemister2 = """Electric Circuit Theory<br />
            Electric Circuit Lab<br />
            Algorithms and Data Structure<br />
            Work Ethics<br />
            Engineering Mathematics II<br />
            Physics II<br />
            Physics Laboratory II<br />
            Language Elective Course II<br />
            Physical Education Elective Course II<br />"""

    listSemister3 = """Statistics for Computer Engineer<br />
            Introduction to Signals and System<br />
            Logic Design of Digital System<br />
            Digital System Design Laboratory<br />
            Software Development Practice I<br />
            Discrete Mathematics<br />
            Science and Maths Elective I<br />"""

    listSemister4 = """Software Development Practice II<br />
            Computer Networks I<br />
            Computer Organization<br />
            Ubiquitous Computing<br />
            Analog and Digital Electronics<br />
            Science and Maths Elective II<br />"""

    listSemister5 = """Software Engineering<br />
            Computer Networks II<br />
            Operating Systems<br />
            Embedded System Design<br />
            Analog and Digital Electronics Lab<br />
            Language Elective Course III<br />"""

    listSemister6 = """Database Systems<br />
            Computer Networks Lab<br />
            Embedded System Design Laboratory<br />
            Language Elective Course IV<br />
            Computer Eng. Elective Course I<br />
            Computer Eng. Elective Course II<br />
            Humanities Elective Course I<br />"""

    listSemister7 = """Project I<br />
            Free Elective Course I<br />
            Humanities Elective Course II<br />
            Computer Eng. Elective Course III<br />
            Computer Eng. Elective Course IV<br />"""

    listSemister8 = """Project II<br />
            Computer Eng. Seminar<br />
            Free Elective Course II<br />
            Science and Maths Elective III"""

    return render(request, 'subject.html', {'semister1':listSemister1,'semister2':listSemister2,'semister3':listSemister3,'semister4':listSemister4,'semister5':listSemister5,'semister6':listSemister6,'semister7':listSemister7,'semister8':listSemister8})
#หน้า Graph
def Graph(request):
    datagpax=[]
    sum_unit=[]
    datagpagraph_term1 = []
    datagpagraph_term2 = []
    datagpagraph_term3 = []
    datagpagraph_term4 = []
    datagpagraph_term5 = []
    datagpagraph_term6 = []
    datagpagraph_term7 = []
    datagpagraph_term8 = []
    #หาค่า Grade แต่ละเทอม เพื่อ plot graph
    for i in Datagrade.objects.all():
        if request.user == i.user:
            if i.term == "1" and i.term != 0:
                try:
                    datagpagraph_term1.append(float(i.GPA))
                except:
                    pass
            if i.term == "2" and i.term != 0:
                try:
                    datagpagraph_term2.append(float(i.GPA))
                except:
                    pass
            if i.term == "3" and i.term != 0:
                try:
                    datagpagraph_term3.append(float(i.GPA))
                except:
                    pass
            if i.term == "4" and i.term != 0:
                try:
                    datagpagraph_term4.append(float(i.GPA))
                except:
                    pass
            if i.term == "5" and i.term != 0:
                try:
                    datagpagraph_term5.append(float(i.GPA))
                except:
                    pass
            if i.term == "6" and i.term != 0:
                try:
                    datagpagraph_term6.append(float(i.GPA))
                except:
                    pass
            if i.term == "7" and i.term != 0:
                try:
                    datagpagraph_term7.append(float(i.GPA))
                except:
                    pass
            if i.term == "8" and i.term != 0:
                try:
                    datagpagraph_term8.append(float(i.GPA))
                except:
                    pass
            #หาค่า GPAX
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade) * float(i.unit))
    print(datagpagraph_term1)
    if sum_unit and datagpax != 0:
        Result_gpax = '%.2f' % (sum(datagpax) / sum(sum_unit))
        return render(request, 'Graph.html', {'Result_gpax': Result_gpax,'datagpagraph_term1':datagpagraph_term1,'datagpagraph_term2':datagpagraph_term2,
                                     'datagpagraph_term3':datagpagraph_term3,'datagpagraph_term4':datagpagraph_term4,
                                     'datagpagraph_term5':datagpagraph_term5,'datagpagraph_term6':datagpagraph_term6,
                                     'datagpagraph_term7':datagpagraph_term7,'datagpagraph_term8':datagpagraph_term8})
    return render(request, 'Graph.html')
#หน้า Result เทอม1
def firstTerm(request):
    datagrade1 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 1
        if request.user == i.user and i.term == "1":
            datagrade1.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade) * float(i.unit))
    #หาค่า GPA
    if sum_unit and datagpax != 0:
        Result_gpax = '%.2f' % (sum(datagpax) / sum(sum_unit))
        return render(request, 'firstTerm.html', {'datagrade1': datagrade1, 'Result_gpax': Result_gpax})
    return render(request, 'firstTerm.html')
#หน้า Result เทอม2
def secondTerm(request):
    datagrade2 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 2
        if request.user == i.user and i.term == "2":
            datagrade2.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade) * float(i.unit))
    if sum_unit and datagpax != 0:
        Result_gpax = '%.2f' % (sum(datagpax) / sum(sum_unit))
        return render(request, 'secondTerm.html', {'datagrade2': datagrade2, 'Result_gpax': Result_gpax})
    return render(request, 'secondTerm.html')
#หน้า Result เทอม3
def thirdTerm(request):
    datagrade3 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 3
        if request.user == i.user and i.term == "3":
            datagrade3.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade)*float(i.unit))
    if sum_unit and datagpax != 0:
        Result_gpax = '%.2f' % (sum(datagpax) / sum(sum_unit))
        return render(request, 'thirdTerm.html', {'datagrade3': datagrade3, 'Result_gpax': Result_gpax})
    return render(request, 'thirdTerm.html')
#หน้า Result เทอม4
def fourthTerm(request):
    datagrade4 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 4
        if request.user == i.user and i.term == "4":
            datagrade4.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade)*float(i.unit))
    if sum_unit and datagpax != 0 :
        Result_gpax = '%.2f' %(sum(datagpax)/sum(sum_unit))
        return render(request, 'fourthTerm.html', {'datagrade4':datagrade4,'Result_gpax':Result_gpax})
    return render(request, 'fourthTerm.html')
#หน้า Result เทอม5
def fifthTerm(request):
    datagrade5 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 5
        if request.user == i.user and i.term == "5":
            datagrade5.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade)*float(i.unit))
    if sum_unit and datagpax != 0 :
        Result_gpax = '%.2f' %(sum(datagpax)/sum(sum_unit))
        return render(request, 'fifthTerm.html', {'datagrade5':datagrade5,'Result_gpax':Result_gpax})
    return render(request, 'fifthTerm.html')
#หน้า Result เทอม6
def sixthTerm(request):
    datagrade6 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 6
        if request.user == i.user and i.term == "6":
            datagrade6.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade)*float(i.unit))
    if sum_unit and datagpax != 0 :
        Result_gpax = '%.2f' %(sum(datagpax)/sum(sum_unit))
        return render(request, 'sixthTerm.html', {'datagrade6':datagrade6,'Result_gpax':Result_gpax})
    return render(request, 'sixthTerm.html')
#หน้า Result เทอม7
def seventhTerm(request):
    datagrade7 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 7
        if request.user == i.user and i.term == "7":
            datagrade7.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade)*float(i.unit))
    if sum_unit and datagpax != 0 :
        Result_gpax = '%.2f' %(sum(datagpax)/sum(sum_unit))
        return render(request, 'seventhTerm.html', {'datagrade7':datagrade7,'Result_gpax':Result_gpax})
    return render(request, 'seventhTerm.html')
#หน้า Result เทอม8
def eightTerm(request):
    datagrade8 = []
    datagpax=[]
    sum_unit=[]
    for i in Datagrade.objects.all():
        # หาค่า Grade ในเทอม 8
        if request.user == i.user and i.term == "8":
            datagrade8.append(i)
        #หาค่า GPAX
        if request.user == i.user:
            if i.Grade != "0" and i.unit != "0":
                sum_unit.append(float(i.unit))
                datagpax.append(float(i.Grade)*float(i.unit))
    if sum_unit and datagpax != 0 :
        Result_gpax = '%.2f' %(sum(datagpax)/sum(sum_unit))
        return render(request, 'eightTerm.html', {'datagrade8':datagrade8,'Result_gpax':Result_gpax})
    return render(request, 'eightTerm.html')
#หน้ารูป Flow
def picFlow(request):
    return render(request, 'picFlow.html')
#หน้า about
def about(request):
    return render(request, 'about.html')
#หน้า help
def help(request):
    return render(request, 'help.html')
