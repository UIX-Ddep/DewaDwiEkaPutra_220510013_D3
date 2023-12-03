import flet as ft

def main(page : ft.page):
    page.title = "Calculator"
    page.window_height = 400
    page.window_width = 300
    page.window_resizable = False
    page.bgcolor = "#000000"

    def keyboard(e):
        data = e.control.data

        if data in ["1","2","3","4","5","6","7","8","9","0",".","+","-","*","/","(",")"]:
            txt.value = str(txt.value) + str(data)
            page.update()

        if data =="=":
            txt.value= str(eval(txt.value))
            page.update()

        if data =="e":
            st = list(txt.value)
            st.pop()
            txt.value = "".join(map(str,st))
            page.update()
        
        if data =="c":
            txt.value = ""
            page.update()

    txt = ft.TextField(
        read_only=True,
        border_color="#FFFFFF",
        text_style= ft.TextStyle(size=50,color="#FFFFFF")
    )

    page.add(txt)

    btn_e = ft.ElevatedButton(
        text = "<", bgcolor="#CCC8AA",color="#000000",data="e",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_po = ft.ElevatedButton(
        text = "(", bgcolor="#CCC8AA",color="#000000",data="(",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_pc = ft.ElevatedButton(
        text = ")", bgcolor="#CCC8AA",color="#000000",data=")",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_division = ft.ElevatedButton(
        text = "÷", bgcolor="#FF9209",color="#FFFFFF",data="/",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
  
    r1 = ft.Row(
        controls=[btn_e,btn_po,btn_pc,btn_division],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )  
   

    btn_7 = ft.ElevatedButton(
        text = "7", bgcolor="#4F4A45",color="#FFFFFF",data="7",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_8 = ft.ElevatedButton(
        text = "8", bgcolor="#4F4A45",color="#FFFFFF",data="8",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_9 = ft.ElevatedButton(
        text = "9", bgcolor="#4F4A45",color="#FFFFFF",data="9",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_multi = ft.ElevatedButton(
        text = "x", bgcolor="#FF9209",color="#FFFFFF",data="*",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
  
    r2 = ft.Row(
        controls=[btn_7,btn_8,btn_9,btn_multi],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )  
   

    btn_4 = ft.ElevatedButton(
        text = "4", bgcolor="#4F4A45",color="#FFFFFF",data="4",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_5 = ft.ElevatedButton(
        text = "5", bgcolor="#4F4A45",color="#FFFFFF",data="5",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_6 = ft.ElevatedButton(
        text = "6", bgcolor="#4F4A45",color="#FFFFFF",data="6",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_sub = ft.ElevatedButton(
        text = "-", bgcolor="#FF9209",color="#FFFFFF",data="-",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
  
    r3 = ft.Row(
        controls=[btn_4,btn_5,btn_6,btn_sub],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )  
 

    btn_1 = ft.ElevatedButton(
        text = "1", bgcolor="#4F4A45",color="#FFFFFF",data="1",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_2 = ft.ElevatedButton(
        text = "2", bgcolor="#4F4A45",color="#FFFFFF",data="2",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_3 = ft.ElevatedButton(
        text = "3", bgcolor="#4F4A45",color="#FFFFFF",data="3",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_sum = ft.ElevatedButton(
        text = "+", bgcolor="#FF9209",color="#FFFFFF",data="+",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
  
    r4 = ft.Row(
        controls=[btn_1,btn_2,btn_3,btn_sum],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )  
   

    btn_c = ft.ElevatedButton(
        text = "C", bgcolor="#CCC8AA",color="#000000",data="c",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_0 = ft.ElevatedButton(
        text = "0", bgcolor="#4F4A45",color="#FFFFFF",data="0",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_dot = ft.ElevatedButton(
        text = ".", bgcolor="#CCC8AA",color="#000000",data=".",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
    btn_eq = ft.ElevatedButton(
        text = "=", bgcolor="#FF9209",color="#FFFFFF",data="=",on_click=keyboard,
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=100))
    )
  
    r5 = ft.Row(
        controls=[btn_c,btn_0,btn_dot,btn_eq],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )  
    page.add(r1,r2,r3,r4,r5)

ft.app(target=main)