Problem -I 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.

 

Problem -II
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.

#Problem 1
def wavelength(n):
    if n in range(380,450):
        return "The colour light is of Violet Wavelength"
    elif n in range(450,495):
        return "The colour of light is of Blue Wavelength"
    elif n in range(495,570):
        return "The colour light is of Green Wavelength"
    elif n in range(570,590):
        return "The colour light is of Yellow Wavelength"
    elif n in range(590,620):
        return "The colour light is of Orange Wavelength"
    elif n in range(620,750):
        return "The colour light is of Red Wavelength"
    elif n<380 or n > 750:
        return "No visible light in the entered Wavelength"

n = int(input())
print(wavelength(n))


#Problem 2
def Radiation(n):
    if n < 3e9:
        return "The entered frequency is a Radio Wave"
    elif 3e9 <= n < 3e12:
        return "The entered frequency is a Microwave"
    elif 3e12 <= n < 4.3e14:
        return "The entered frequency is a Infrared Light "
    elif 4.3e14 <= n < 7.5e14:
        return "The entered frequency is a Visible Light"
    elif 7.5e14 <= n < 3e17:
        return "The entered frequency is a Ultraviolet Light"
    elif 3e17 <= n < 3e19:
        return "The entered frequency is a X-Ray"
    elif n >= 3e19:
        return "The entered frequency is a Gamma Ray"

n = float(input())
print(Radiation(n))

