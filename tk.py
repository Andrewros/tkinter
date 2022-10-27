import tkinter as tk


def dollars_to_float(price):
    num_price = ""
    for letter in price:
        if letter == "$":
            pass
        else:
            num_price += letter
    num_price = float(num_price)
    return num_price


def percent_to_float(percentage):
    float_percentage = ""
    for letter in percentage:
        if letter == "%":
            pass
        else:
            float_percentage += letter
    float_percentage = float(float_percentage)
    return float_percentage


def main():
    window = tk.Tk()
    window.title("Tip")
    window.minsize(width=500, height=350)
    price_label = tk.Label(text="Price:")
    price_label.pack()
    price = tk.Entry(window)
    price.pack()
    percent_label = tk.Label(text="What percentage would you like to tip?")
    percent_label.pack()
    percent = tk.Entry(window)
    percent.pack()

    def button_clicked():
        num_price = dollars_to_float(price.get())
        float_percentage = percent_to_float(percent.get())
        tip = round(num_price*(float_percentage/100), 2)
        tip = str(tip)
        tips = tip.split(".")
        if len(tips[1]) == 1:
            tips[1] += "0"
            tip = ".".join(tips)
        tip_number.config(text=f"Leave ${tip}")

    submit = tk.Button(text="Add", command=button_clicked)
    submit.pack()
    tip_number = tk.Label(text="")
    tip_number.pack()
    window.mainloop()


if __name__ == "__main__":
    main()
