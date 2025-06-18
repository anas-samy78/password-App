from flet import *
import random
import string

def main(page: Page):
    # واجهة التطبيق الأساسية 
    page.title = "Anas Samy"
    page.window.width = 370
    page.window.height = 700
    page.bgcolor = Colors.WHITE  
    page.window.top = 10
    page.window.left = 450
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.scroll = 'auto'
    
    # المتغيرات
    tot = TextField(label="أدخل طول كلمة السر")
    letters = TextField(label="أدخل عدد الأحرف")
    numbers = TextField(label="أدخل عدد الأرقام")
    symbols = TextField(label="أدخل عدد علامات الترقيم")
    
    result_text = Text("", size=19, color=Colors.BLACK,width=390,text_align="center",weight=FontWeight.BOLD)  
    result1_text =  Text("", size=16, color=Colors.BLACK)
    # دالة إنشاء كلمة السر
    def password(e):
        try:
            total = int(tot.value)
            num_letters = int(letters.value)
            num_numbers = int(numbers.value)
            num_symbols = int(symbols.value)

            if total == num_letters + num_numbers + num_symbols:
                letters_1 = random.choices(string.ascii_letters, k=num_letters)
                numbers_1 = random.choices(string.digits, k=num_numbers)
                symbols_1 = random.choices(string.punctuation, k=num_symbols)

                full_password = letters_1 + numbers_1 + symbols_1
                random.shuffle(full_password)

                password_str = "".join(full_password)
                
                # تحديث النص المعروض لعرض كلمة السر
                result_text.value = f"Your password is: {password_str}"
                result1_text.value = f"{password_str}"
                
            else:
                result_text.value = "❌ طول كلمة السر غير مساوي لمجموع الأحرف والأرقام وعلامات الترقيم"
                result_text.color = Colors.RED  

            page.update()  
        except ValueError:
            result_text.value = "⚠️ تأكد من إدخال أرقام صحيحة فقط!"
            result_text.color = Colors.ORANGE  
            page.update()  
    def copy_password(e):
        v1 = result1_text.value
        if  v1:
            page.set_clipboard(result1_text.value)
            mas =  AlertDialog(
                    title=Text("تم نسخ كلمة المرور" , color=Colors.GREEN , size=18)
            )
            page.add(mas)
            mas.open=True
            page.update()
        else:   
            mas =  AlertDialog(
                    title=Text("ليست هناك كلمة مرور لحذفها" , color=Colors.RED , size=18)
            )
            page.add(mas)
            mas.open=True
            page.update()
        page.update()
    # الواجهات
    def show_pages(v):
        page.views.clear()
        page.views.append(View("/",[
            AppBar(title=Text("تطبيق منشئ كلمات سر قوية",size=24,color=Colors.WHITE,width=390,text_align="center",weight=FontWeight.BOLD),
                   bgcolor=Colors.BLUE 
                   ),
            Row([Image(src="صور/pngwing.com (9).png",width=330,height=350)],alignment=MainAxisAlignment.CENTER),
            ElevatedButton("أنشئ كلمة سر قوية الآن",color=Colors.WHITE,bgcolor=Colors.PURPLE,width=350,height=50,on_click=lambda e:page.go("/pass"))
        ],bgcolor=Colors.BLUE_GREY_900))  

        if page.route == "/pass":
            page.views.append(View("/pass",[
                AppBar(title=Text("password".upper(),size=24,color=Colors.WHITE,width=390,text_align="center",weight=FontWeight.BOLD),
                   bgcolor=Colors.BLUE  
                   ),
                tot, letters, numbers, symbols, result_text,
                
                ElevatedButton("copy".upper(),on_click=copy_password,icon=Icons.COPY),
                ElevatedButton("اضغط للإنشاء",color=Colors.PURPLE, width=350, height=50, on_click=password,bgcolor=Colors.BLUE_200)
            ]))

        page.update()
    def page_go(g):
        page.views.pop()
        go_p = page.views[-1]
        page.go(go_p.route)
    
    page.update()
    page.on_route_change = show_pages
    page.on_view_pop = page_go
    page.go(page.route)

app(main)
