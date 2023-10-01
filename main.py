import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)

    except:
        text_result.delete(1.0,"end")
        text_result.insert(1.0,"Error")



def delete_calculation():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")


root = tk.Tk()
root.title(string='Calculator')
root.geometry("400x600")

text_result = tk.Text(root,height=5,width=25,font=("Courier",20,"bold"))
text_result.grid(row=1,columnspan=5)

btn1 = tk.Button(root,text="1",width=5,command=lambda:add_to_calculation(1),font=("Courier",14,"bold"))
btn1.grid(row=2,column=0)
btn2 = tk.Button(root,text="2",width=5,command=lambda:add_to_calculation(2),font=("Courier",14,"bold"))
btn2.grid(row=2,column=1)
btn3 = tk.Button(root,text="3",width=5,command=lambda:add_to_calculation(3),font=("Courier",14,"bold"))
btn3.grid(row=2,column=2)
btn4 = tk.Button(root,text="4",width=5,command=lambda:add_to_calculation(4),font=("Courier",14,"bold"))
btn4.grid(row=3,column=0)
btn5 = tk.Button(root,text="5",width=5,command=lambda:add_to_calculation(5),font=("Courier",14,"bold"))
btn5.grid(row=3,column=1)
btn6 = tk.Button(root,text="6",width=5,command=lambda:add_to_calculation(6),font=("Courier",14,"bold"))
btn6.grid(row=3,column=2)
btn7 = tk.Button(root,text="7",width=5,command=lambda:add_to_calculation(7),font=("Courier",14,"bold"))
btn7.grid(row=4,column=0)
btn8 = tk.Button(root,text="8",width=5,command=lambda:add_to_calculation(8),font=("Courier",14,"bold"))
btn8.grid(row=4,column=1)
btn9 = tk.Button(root,text="9",width=5,command=lambda:add_to_calculation(9),font=("Courier",14,"bold"))
btn9.grid(row=4,column=2)

btn_plus = tk.Button(root,text="+",width=5,command=lambda:add_to_calculation("+"),font=("Courier",14,"bold"))
btn_plus.grid(row=2,column=3)
btn_minus = tk.Button(root,text="-",width=5,command=lambda:add_to_calculation("-"),font=("Courier",14,"bold"))
btn_minus.grid(row=3,column=3)
btn_mul = tk.Button(root,text="*",width=5,command=lambda:add_to_calculation("*"),font=("Courier",14,"bold"))
btn_mul.grid(row=4,column=3)
btn_div = tk.Button(root,text="/",width=5,command=lambda:add_to_calculation("/"),font=("Courier",14,"bold"))
btn_div.grid(row=5,column=3)
btn_equal = tk.Button(root,text="=",width=13,command=evaluate_calculation,font=("Courier",14,"bold"))
btn_equal.grid(row=6,column=2,columnspan=2)
btn_left_brace = tk.Button(root,text="(",width=5,command=lambda:add_to_calculation("("),font=("Courier",14,"bold"))
btn_left_brace.grid(row=5,column=0)
btn_right_brace = tk.Button(root,text=")",width=5,command=lambda:add_to_calculation(")"),font=("Courier",14,"bold"))
btn_right_brace.grid(row=5,column=2)

btn_zero = tk.Button(root,text="0",width=5,command=lambda:add_to_calculation("0"),font=("Courier",14,"bold"))
btn_zero.grid(row=5,column=1)
btn_clear = tk.Button(root,text="C",width=6,command=delete_calculation,font=("Courier",18,"bold"))
btn_clear.grid(row=6,column=0)
btn_dot = tk.Button(root,text=".",width=5,command=lambda:add_to_calculation("."),font=("Courier",14,"bold"))
btn_dot.grid(row=6,column=1)


canvas = tk.Canvas(root, width=200, height=200)
canvas.grid(row=0, column=0, columnspan=5)

# Load and display the image on the Canvas
image_path = "images.png"
image = tk.PhotoImage(file=image_path)
canvas.create_image(100,100 ,anchor='center', image=image)

root.mainloop()