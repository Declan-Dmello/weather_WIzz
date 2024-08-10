from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
# from data3 import data1
from extra_info import *
import matplotlib.ticker as plticker
import matplotlib.pyplot as plt

#plt.ylim((25,250))

window = Tk()

# setting the title
window.title('Plotting in Tkinter')

# dimensions of the main window
window.geometry("500x500")

def plotting():

    # the figure that will contain the plot
    fig = Figure(figsize=(15, 6),
                 dpi=95)

    # list of squares
    # y = [i ** 2 for i in range(101)]
    y = data1.values()
    x = data1.keys()

    # adding the subplot
    plot1 = fig.add_subplot(211)

    plot1.set_title("Per Hour Temperature")

    plot1.set_xlabel("Time of Day")

    plot1.set_ylabel("Temperature ")

    loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
    plot1.xaxis.set_major_locator(loc)
    # plotting the graph

    plot1.plot(x, y, color='orange', marker='o')

    for x, y in zip(x, y):
        label = "{}".format(y)
        plot1.annotate(label, xy=(x, y), textcoords='offset points', xytext=(0, 10), ha='center')


    # creating the Tkinter canvas
    # containing the Matplotlib figure

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()


    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().place(x=-80, y=340)



Button1 = Button(window,command= plotting, text="temp")
Button1.pack()



def plotting1():
    fig1 = plt.figure(figsize=(15, 6), dpi=95)

    # list of squares
    # y = [i ** 2 for i in range(101)]
    y = list(data1.values())
    x = list(data1.keys())
    plot1 = fig1.add_subplot(211)

    plot1.bar(x, y, color='blue',
              width=0.8)
    # adding the subplot
    # plot1 = fig1.add_subplot(111)

    # creating the bar plot

    plot1.set_title("Per Hour Precipitation Probability")

    plot1.set_xlabel("Time of Day")

    plot1.set_ylabel("Precipitation Probability %")

    loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
    plot1.xaxis.set_major_locator(loc)
    for bar in plot1.patches:
         plot1.annotate(format(bar.get_height(), ''),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
    # plotting the graph
    #  plt.show()

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas1 = FigureCanvasTkAgg(fig1, master=window)

    canvas1.draw()

    # placing the canvas on the Tkinter window

    # placing the toolbar on the Tkinter window
    canvas1.get_tk_widget().place(x=-80, y=340)

    #the figure that will contain the plot
 #    fig1 = Figure(figsize=(5, 5),dpi=90)





Button2 = Button(window,command= plotting1, text="Plot2")
Button2.pack()





def plotting2():
    fig2 = plt.figure(figsize=(15, 6), dpi=95)

    # list of squares
    # y = [i ** 2 for i in range(101)]
    y = list(data1.values())
    x = list(data1.keys())
    plot2 = fig2.add_subplot(211)

    plot2.bar(x, y, color='#ADD8E6',
              width=0.8)
    # adding the subplot
    # plot1 = fig1.add_subplot(111)

    # creating the bar plot

    plot2.set_title("Per Hour Precipitation Probability")

    plot2.set_xlabel("Time of Day")

    plot2.set_ylabel("Wind speed ")

    loc = plticker.MultipleLocator(base=1.0)  # this locator puts ticks at regular intervals
    plot2.xaxis.set_major_locator(loc)
    for bar in plot2.patches:
         plot2.annotate(format(bar.get_height(), ''),
                   (bar.get_x() + bar.get_width() / 2,
                    bar.get_height()), ha='center', va='center',
                   size=10, xytext=(0, 8),
                   textcoords='offset points')
    # plotting the g2raph
    #  plt.show()

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas2 = FigureCanvasTkAgg(fig2, master=window)

    canvas2.draw()

    # placing the canvas on the Tkinter window

    # placing the toolbar on the Tkinter window
    canvas2.get_tk_widget().place(x=-80, y=340)

    #the figure that will contain the plot
 #    fig1 = Figure(figsize=(5, 5),dpi=90)





Button3 = Button(window,command= plotting2, text="wind")
Button3.pack()


window.mainloop()
