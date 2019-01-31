#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BlankClass(object):
    '''This is a Blank class for CS162.'''
    pass
t = BlankClass()

class ClassWithAttr(object):
    x1 = 1
    x2 = 2

my_attr = ClassWithAttr()
my_attr.x3 = 3


# In[2]:


help(t)


# In[3]:


type(t)


# In[4]:


dir(t)


# In[5]:


hash(t)


# In[6]:


id(t)


# In[7]:


hasattr(my_attr,'x3')


# In[8]:


getattr(my_attr,'x3')


# In[13]:


delattr(my_attr,'x3')


# In[10]:


vars(my_attr)


# In[12]:


bool(t)


# ### Build up a list of all the classes defined in the tkinter library, and all the parent classes that it inherits from
# 
# class Event
# class Variable
# class Pack
# class XView
# class YView
# class Wm
# class Place
# class Grid
# class Image
# class BaseWidget(Misc) - inherits from class Misc
# class Widget(BaseWidget, Pack, Place, Grid) - inherits from classes Place, Grid, Pack, BaseWidget
# class Toplevel(BaseWidget, Wm) - inherits from classes Basewidget and Wm
# class Button(Widget) - inherits from class Widget
# class Canvas(Widget, XView, YView) - inherits from classes Widget, XView and YView
# class Checkbutton(Widget)
# class Entry(Widget, XView)
# class Frame(Widget)
# class Label(Widget)
# class Menu(Widget)
# class Menubutton(Widget)
# class Message(Widget
# class Radiobutton(Widget)
# class Scale(Widget)
# class Scrollbar(Widget)
# class Text(Widget, XView, YView)
# class OptionMenu(Menubutton)
# class PhotoImage(Image)
# class BitmapImage(Image)
# class Spinbox(Widget, XView)
# class LabelFrame(Widget)
# class PanedWindow(Widget)
# class Listbox(Widget, XView, YView)
# class Tk(Misc, Wm) - inherits from class Wm and class Misc
# class StringVar(Variable) - inherits from class Variable
# class IntVar(Variable) - inherits from class Variable
# class DoubleVar(Variable) - inherits from class Variable
# class BooleanVar(Variable) - inherits from class Variable
# class Misc - internal class under class BooleanVar
# class CallWrapper - internal class 

# ### Now choose a class that inherits from widget and list all the methods that one can call on that widget
# 
# class Button(Widget)
# def destroy
# def do
# def pack_configure
# def pack_forget
# def pack_info
# def place_configure
# def place_forget
# def place_info
# def grid_configure
# def grid_forget
# def grid_remove
# def grid_info

# ### Find a simple online tutorial on tkinter and build a simple graphical user interface.  How much of the complexity of the library can be hidden from an enduser?

# In[ ]:


from tkinter import * 
window = Tk()
window.title("Welcome to LikeGeeks app") 
window.mainloop()


# In[ ]:




