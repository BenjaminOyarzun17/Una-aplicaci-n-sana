 

import tkinter as tk
import json as js 
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
#import numpy as np
import os 
import datetime 
import time
from functools import partial





class v1:
    def __init__(self, master):
        self.master = master
        master.geometry("700x500")
        master.title("Una Aplicación Sana")
        self.cajaOpciones= tk.Canvas(self.master, height = 250, width = 350)
        self.intrucciones = tk.Label(self.cajaOpciones,
                                text="Seleccione la actividad que quiere realizar\n",
                                font=("Arial", 24))
        
        self.b1 = tk.Button(self.cajaOpciones, 
                       text= "temporizador", 
                       command = self.vtimer, 
                       width = 25, 
                       height= 3, 
                       font=("Arial", 12))
        self.b2 = tk.Button(self.cajaOpciones, 
                       text= "visualizador diario", 
                       width = 25, 
                       height= 3, 
                       font=("Arial", 12),
                       command = self.vGrafDia)
        self.b3 = tk.Button(self.cajaOpciones, 
                       text= "visualizador semanal", 
                       command = self.vGrafSemana, 
                       width = 25, 
                       height= 3, 
                       font=("Arial", 12))
        self.b4 = tk.Button(self.cajaOpciones,
                            text = "visualizador semana anterior",
                            command = self.vGrafSemanaA, 
                            width = 25, 
                            height= 3, 
                            font=("Arial", 12))
        self.b5 = tk.Button(self.cajaOpciones, 
                            text = "determinar actividades",
                            command = self.determinador,
                            width = 25, 
                            height= 3, 
                            font=("Arial", 12))
        
        #self.b4 = tk.Button(self.cajaOpciones, 
         #              text= "", 
          #             command = self.descargar_datos, 
           #            width = 21, 
            #           height= 3, 
             #          font=("Arial", 12))
        self.cajaOpciones.place(x=80, y=50)
        self.intrucciones.grid(sticky = "N")
        self.b1.grid()
        self.b2.grid()
        self.b3.grid()
        self.b4.grid()
        self.b5.grid()
        #self.b4.grid()   
        self.horas = 0
        self.minutos = 0
        self.segundos = 1
        #self.TEstudio = tk.StringVar()
        self.TEstudio = ""
        self.TDescanso = ""
        self.TClase = ""
        self.estado = tk.BooleanVar() #quizas hay qe definir esto arriba...
        self.estado.set(False)
    def determinador(self):
        
        self.estudiosPerson = []
        estudiosPersonJson={"Tipo":"Estudio",
                                 "Actividades": self.estudiosPerson}
        self.clasePerson = []
        clasePersonJson={"Tipo": "Clase",
                            "Actividades":self.clasePerson}
        self.descansoPerson = []
        descansoPersonJson = {"Tipo": "Descanso",
                                 "Actividades":self.descansoPerson}
        
         
        def appendear():            
            self.estudiosPerson = []
            
            self.clasePerson = []
            
            self.descansoPerson = []
            
            json_data = []
            with open('Actividades.txt', 'r') as file:
                for line in file:
                    json_line = js.loads(line)
                    json_data.append(json_line)
                    print(json_line)
                file.close()
            
            for dato in json_data:
                if dato["Tipo"]== "Clase":
                    self.clasePerson = dato["Actividades"]
                    
                if dato["Tipo"]== "Estudio":
                    self.estudiosPerson= dato["Actividades"]
                if dato["Tipo"]== "Descanso":
                    self.descansoPerson= dato["Actividades"]
                    print(dato["Actividades"])
            
            if self.EntryEstudio.get() != "":
                self.estudiosPerson.append(self.EntryEstudio.get())
                 
            if self.EntryClase.get() != "":
                self.clasePerson.append(self.EntryClase.get())
            if self.EntryDescanso.get() != "":
                self.descansoPerson.append(self.EntryDescanso.get())
            
            estudiosPersonJson={"Tipo":"Estudio",
                                     "Actividades": self.estudiosPerson}
            clasePersonJson={"Tipo": "Clase",
                                "Actividades":self.clasePerson}
            descansoPersonJson = {"Tipo": "Descanso",
                                     "Actividades":self.descansoPerson}
            open('Actividades.txt', 'w').close()
            with open('Actividades.txt', 'a') as file:
                js.dump(estudiosPersonJson,file)
                file.write("\n")
                js.dump(clasePersonJson,file) 
                file.write("\n")
                js.dump(descansoPersonJson,file)
        def reset():
            def warning():
                def estado():
                     
                    open('Actividades.txt', 'w').close()
                     
                def cancelar():
                    win.destroy()
                     
                win = tk.Toplevel()
                win.title("Información importante")
                message = "al proceder, se borrarán las actividades guardadas"
                Label1 = tk.Label(win, text=message)
                Label1.grid(column = 0, row = 0)
                canvas1 = tk.Canvas(win)
                canvas1.grid(column = 0, row = 1)
                btn2 = tk.Button(canvas1, text='Proceder', command = estado)
                btn2.grid(column = 0, row = 0)
                btn1 = tk.Button(canvas1, text='Cancelar', command = cancelar)
                btn1.grid(column = 1, row = 0)
              
            warning()
            
                
        def showActivity():
            json_data = []
            EstudioIngresado =[]
            ClaseIngresado = []
            DescansoIngresado =[]
            with open('Actividades.txt', 'r') as file:
                for line in file:
                    json_line = js.loads(line)
                    json_data.append(json_line)
            for elemento in json_data:
                if elemento["Tipo"] == "Estudio":
                    EstudioIngresado = elemento["Actividades"]
                    print(EstudioIngresado)
                if elemento["Tipo"] == "Clase":
                    ClaseIngresado = elemento["Actividades"]
                    print(ClaseIngresado)
                if elemento["Tipo"] == "Descanso":
                    DescansoIngresado = elemento["Actividades"]
                    print(DescansoIngresado)
            for estudio in EstudioIngresado:
                tk.Label(self.vDet,text = estudio,font = ("Arial",20)).grid(column = 1, row = EstudioIngresado.index(estudio)+1)
                                    
            for clase in ClaseIngresado:
                tk.Label(self.vDet,text = clase, font = ("Arial",20)).grid(column = 2, row = ClaseIngresado.index(clase)+1)
            for descanso in DescansoIngresado:
                tk.Label(self.vDet, text = descanso,  font = ("Arial",20)).grid(column = 3, row = DescansoIngresado.index(descanso)+1)
        self.vDet = tk.Toplevel()
        self.vDet.geometry("700x400")
        self.LblActEstudio = tk.Label(self.vDet, 
                                      text = "Ingresa un estudio",
                                      font = ("Arial", 20))
        self.EntryEstudio=tk.Entry(self.vDet)
        self.btnReset = tk.Button(self.vDet,
                                    text = "Reset",
                                    font = ("Arial",20),
                                    command = partial(reset),
                                    width = 20)
        self.LblActClase=tk.Label(self.vDet,
                                  text = "Ingresa una clase",
                                      font = ("Arial", 20))
        self.EntryClase=tk.Entry(self.vDet)
        
        self.LblActDescanso = tk.Label(self.vDet,
                                       text = "Ingresa un descanso",
                                      font = ("Arial", 20))
         
        self.btnMostrarEntry = tk.Button(self.vDet,
                                         text = "Mostrar actividades",
                                         font = ("Arial", 20),
                                         width = 20, command = showActivity)
        self.agregarAct = tk.Button(self.vDet,
                                         text = "Agregar actividad",
                                         font = ("Arial", 20),
                                         width = 20,
                                         command = appendear)
        self.lblEstudio = tk.Label(self.vDet, text = "Estudios",
                                         font = ("Arial", 20))
        self.lblClase= tk.Label(self.vDet, text = "|Clases",
                                         font = ("Arial", 20))
        self.lblDescanso = tk.Label(self.vDet, text = "|Descansos",
                                         font = ("Arial", 20))
        self.EntryDescanso =tk.Entry(self.vDet)
    
        
        self.LblActEstudio.grid(column =0, row = 0)
        self.EntryEstudio.grid(column =0 , row = 1)
        self.btnReset.grid(column = 0, row = 8)
        self.LblActClase.grid(column =0, row =2)
        self.EntryClase.grid(column = 0, row = 3)
        self.LblActDescanso.grid(column = 0, row = 4)
        self.EntryDescanso.grid(column = 0, row = 5)
        self.btnMostrarEntry.grid(column = 0, row = 7)
        self.agregarAct.grid(column = 0, row = 6)
        self.lblEstudio.grid(column = 1, row = 0)
        self.lblClase.grid(column = 2, row = 0) 
        self.lblDescanso.grid(column = 3, row = 0)
    def vGrafSemana(self):
        def showActivity():
            json_data = []
            self.EstudioIngresado =[]
            self.ClaseIngresado = []
            self.DescansoIngresado =[]
            with open('Actividades.txt', 'r') as file:
                for line in file:
                    json_line = js.loads(line)
                    json_data.append(json_line)
            for elemento in json_data:
                if elemento["Tipo"] == "Estudio":
                    self.EstudioIngresado = elemento["Actividades"]
                    print(self.EstudioIngresado)
                if elemento["Tipo"] == "Clase":
                    self.ClaseIngresado = elemento["Actividades"]
                    print(self.ClaseIngresado)
                if elemento["Tipo"] == "Descanso":
                    self.DescansoIngresado = elemento["Actividades"]
                    print(self.DescansoIngresado)
            return self.EstudioIngresado, self.ClaseIngresado,self.DescansoIngresado
        showActivity()
        self.actividadesDeEstudio = self.EstudioIngresado
        self.clases = self.ClaseIngresado
        self.descansos= self.DescansoIngresado        


        self.grafSemanaA = tk.Toplevel()
        self.grafSemanaA.geometry("1700x750")
        self.currentDT = datetime.datetime.now()
        self.fecha = self.currentDT.strftime("%d")
        self.diaSemana = self.currentDT.strftime("%A")
        self.mes = self.currentDT.strftime("%B")
        self.numeroSemanaOriginal= self.currentDT.isocalendar()[1] 
        self.numeroSemana = self.numeroSemanaOriginal
        self.json_data = []
        self.json_file = "DATA.txt"
        self.file = open(self.json_file, "r")
        
        
        for self.line in self.file:
            self.json_line = js.loads(self.line)
            self.json_data.append(self.json_line)
        self.file.close()
        
        
        #conjuntos
        self.setEstudio = []
        self.setClase = []
        self.setDescanso = []
        
        setsEstudio = {}
        setsDescanso = {}
        setsClase={}
        
        for estudio in self.EstudioIngresado:
            setsEstudio[estudio] = []
        for descanso in self.DescansoIngresado:
            setsDescanso[descanso]=[]
        for clase in self.ClaseIngresado:
            setsClase[clase]=[]
        setsEstudioKey = setsEstudio.keys()
        setsDescansoKey = setsDescanso.keys()
        setsClaseKey = setsClase.keys()
        
        for actividad in self.json_data:
            if actividad["Tiempo"]["numero semana"] == self.numeroSemana: #self.numeroSemana
                if actividad["Tipo Espec\u00edfico"]["Estudio"] != "":
                    self.setEstudio.append([actividad["Tipo Espec\u00edfico"]["Estudio"], actividad["Tiempo"]["Duracion"]])
                elif actividad["Tipo Espec\u00edfico"]["Clase"]!="":
                    self.setClase.append([actividad["Tipo Espec\u00edfico"]["Clase"], actividad["Tiempo"]["Duracion"]])


                elif actividad["Tipo Espec\u00edfico"]["descanso:"] != "":
                    self.setDescanso.append([actividad["Tipo Espec\u00edfico"]["descanso:"], actividad["Tiempo"]["Duracion"]])
        
        
       
        
        for par in self.setEstudio:
            for key in setsEstudioKey:
                if par[0] == key:
                    setsEstudio[key].append(par[1])
        for par in self.setClase:
            for key in setsClaseKey:
                if par[0] == key:
                    setsClase[key].append(par[1])
                    
        for par in self.setDescanso:
            for key in setsDescansoKey:
                if par[0] == key:
                    setsDescanso[key].append(par[1])
       
        print(setsDescanso)
        print(setsClase)        
        print(setsEstudio)
        for clase in setsClase:
            setsClase[clase]= sum(setsClase[clase])
        for estudio in setsEstudio:
            setsEstudio[estudio] = sum(setsEstudio[estudio])
        for descanso in setsDescanso:
            setsDescanso[descanso] = sum(setsDescanso[descanso])
       
        print("sumas:")
        print(setsDescanso)
        print(setsClase)
        print(setsEstudio)
        self.tiemposDescanso = []
        self.tiemposEstudio = []
        self.tiemposClase = []
        for descanso in setsDescanso:
            self.tiemposDescanso.append(setsDescanso[descanso])
        for estudio in setsEstudio:
            self.tiemposEstudio.append(setsEstudio[estudio])
        for clase in setsClase:
            self.tiemposClase.append(setsClase[clase])
        print(self.tiemposDescanso)
        print(self.tiemposClase)
        print(self.tiemposEstudio)
        self.tiempoPorTipo = []
        self.tiempoSemanalDescansoTotalSuma = sum(self.tiemposDescanso)
        self.tiempoSemanalEstudioTotalSuma = sum(self.tiemposEstudio)
        self.tiempoSemanalClaseTotalSuma = sum(self.tiemposClase)
        self.tiempoPorTipo.append(self.tiempoSemanalDescansoTotalSuma)
        self.tiempoPorTipo.append(self.tiempoSemanalClaseTotalSuma)
        self.tiempoPorTipo.append(self.tiempoSemanalEstudioTotalSuma)
       
        
        self.tipoActividadEspecifico = ["Descanso", "Clases", "Estudio"]
        
        
        
        self.tiempoSemanalEstudioTotalSumaPromedioPorDia = round(self.tiempoSemanalEstudioTotalSuma/7,2)

        self.tiempoSemanalClaseTotalSumaPromedioPorDia = round(self.tiempoSemanalClaseTotalSuma/7,2)
        self.tiempoSemanalDescansoTotalSumaPromedioPorDia = round(self.tiempoSemanalDescansoTotalSuma/7,2)
        def minutosAHORA(minutos):
            horas = minutos/60
            rondeo = round(horas, 2)
            return rondeo
        self.ClaseEnHoras = minutosAHORA(self.tiempoSemanalClaseTotalSuma)    
        self.EstudioEnHoras = minutosAHORA(self.tiempoSemanalEstudioTotalSuma)
        self.DescansoEnHoras = minutosAHORA(self.tiempoSemanalDescansoTotalSuma) 
        print("en horas: "+ str(self.DescansoEnHoras ))
        print(str(self.tiempoSemanalEstudioTotalSumaPromedioPorDia))
        print(str(self.tiempoSemanalClaseTotalSumaPromedioPorDia))
        print(str(self.tiempoSemanalDescansoTotalSumaPromedioPorDia))
        
        
        
        while len(self.actividadesDeEstudio) > len(self.tiemposEstudio):
            self.tiemposEstudio.append(0)
        while len(self.clases) >len(self.tiemposClase):
            self.tiemposClase.append(0)
            
        while len(self.descansos ) >len(self.tiemposDescanso):
            self.tiemposClase.append(0)
            
            
        self.llbTTAL = tk.Label(self.grafSemanaA,
                                text = "Tiempo utilizado en cada estudio de esta semana",
                                font=("Arial", 20) )
        self.fplot = Figure(figsize = (10,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.actividadesDeEstudio,self.tiemposEstudio,color = "c")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column = 0)
        self.llbTTAL.grid(row=0, column = 0)
        
        self.llbTTALL = tk.Label(self.grafSemanaA,
                                 text = "Tiempo utilizado en cada clase de esta semana" ,
                                font=("Arial", 20))
        self.fplot = Figure(figsize = (10,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.clases,self.tiemposClase,color = "r")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3, column = 0)
        self.llbTTALL.grid(row=2, column = 0)
        
        self.llbTTALLL = tk.Label(self.grafSemanaA,
                                  text = "Tiempo utilizado en cada descanso de esta semana",
                                font=("Arial", 20) )
        self.fplot = Figure(figsize = (10,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.descansos,self.tiemposDescanso,color = "g")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5, column = 0)
        self.llbTTALLL.grid(row=4, column = 0)
        
        self.llbTTALLLL = tk.Label(self.grafSemanaA,
                                  text = "Tiempo utilizado en cada actividad de la semana pasada",
                                font=("Arial", 20) )
        self.fplot = Figure(figsize = (5,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.tipoActividadEspecifico,self.tiempoPorTipo,color = "k")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column = 1)
        self.llbTTALLLL.grid(row=0, column = 1)
        
        print("El promedio de estudio semanal es "+ str(self.tiempoSemanalEstudioTotalSumaPromedioPorDia))

        self.CanvasTabla = tk.Canvas(self.grafSemanaA)
        self.LabelStat1 = tk.Label(self.CanvasTabla,
                                   text = "Promedio (tEstudio/dia): ",
                                   font = ("arial", 17))
        self.LabelStat2 = tk.Label(self.CanvasTabla,
                                   text = "Promedio (tDescanso/dia): ",
                                   font = ("arial", 17))
        self.LabelStat3 = tk.Label(self.CanvasTabla,
                                   text = "Promedio (tClase/dia): ", 
                                   font = ("arial", 17))
        self.LabelStat1_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalEstudioTotalSumaPromedioPorDia)+" minutos",
                                     font = ("arial", 17))
        self.LabelStat2_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalClaseTotalSumaPromedioPorDia)+" minutos",
                                     font = ("arial", 17))
        self.LabelStat3_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalDescansoTotalSumaPromedioPorDia)+" minutos",
                                     font = ("arial", 17))
        self.LabelStat4 = tk.Label(self.CanvasTabla,
                                   text =  "Tiempo total de estudio: ",
                                   font = ("arial", 17))
        self.LabelStat5   =tk.Label(self.CanvasTabla,
                                    text =  "Tiempo total en clases: ",
                                    font = ("arial", 17))
        self.LabelStat6   = tk.Label(self.CanvasTabla,
                                     text =  "Tiempo total descansando: ",
                                     font = ("arial", 17))
        self.LabelStat4_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalEstudioTotalSuma)+ " minutos o " +str(self.EstudioEnHoras)+" horas",
                                     font = ("arial", 17))
        self.LabelStat5_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalClaseTotalSuma)+ " minutos o "+str(self.ClaseEnHoras)+" horas",
                                     font = ("arial", 17))
        self.LabelStat6_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalDescansoTotalSuma)+ " minutos o "+str(self.DescansoEnHoras)+" horas",
                                     font = ("arial", 17))
        
        self.CanvasTabla.grid(row = 2, column =1, rowspan = 4)
        self.LabelStat1.grid(row = 0, column = 0)
        self.LabelStat2.grid(row= 1, column = 0)
        self.LabelStat3.grid(row = 2, column = 0)
        self.LabelStat1_1.grid(row = 0, column = 1)
        self.LabelStat2_1.grid(row = 1, column = 1)
        
        self.LabelStat3_1.grid(row = 2,column = 1)
        
        self.LabelStat4.grid(row = 3,column = 0)
        self.LabelStat5.grid(row = 4,column = 0)
        self.LabelStat6.grid(row = 5,column = 0)
        self.LabelStat4_1.grid(row = 3,column = 1)
        self.LabelStat5_1.grid(row = 4,column = 1)
        self.LabelStat6_1.grid(row = 5,column = 1)

        print(self.setEstudio)
        print(self.setClase)      
        print(self.setDescanso)    
    def vGrafSemanaA(self):
        def showActivity():
            json_data = []
            self.EstudioIngresado =[]
            self.ClaseIngresado = []
            self.DescansoIngresado =[]
            with open('Actividades.txt', 'r') as file:
                for line in file:
                    json_line = js.loads(line)
                    json_data.append(json_line)
            for elemento in json_data:
                if elemento["Tipo"] == "Estudio":
                    self.EstudioIngresado = elemento["Actividades"]
                    print(self.EstudioIngresado)
                if elemento["Tipo"] == "Clase":
                    self.ClaseIngresado = elemento["Actividades"]
                    print(self.ClaseIngresado)
                if elemento["Tipo"] == "Descanso":
                    self.DescansoIngresado = elemento["Actividades"]
                    print(self.DescansoIngresado)
            return self.EstudioIngresado, self.ClaseIngresado,self.DescansoIngresado
        showActivity()
        self.grafSemanaA = tk.Toplevel()
        self.grafSemanaA.geometry("1700x750")
        self.currentDT = datetime.datetime.now()
        self.fecha = self.currentDT.strftime("%d")
        self.diaSemana = self.currentDT.strftime("%A")
        self.mes = self.currentDT.strftime("%B")
        self.numeroSemanaOriginal= self.currentDT.isocalendar()[1] 
        self.numeroSemana = self.numeroSemanaOriginal -1
        self.json_data = []
        self.json_file = "DATA.txt"
        self.file = open(self.json_file, "r")
        
        
        for self.line in self.file:
            self.json_line = js.loads(self.line)
            self.json_data.append(self.json_line)
        self.file.close()
        
        
        #conjuntos
        self.setEstudio = []
        self.setClase = []
        self.setDescanso = []
        
        setsEstudio = {}
        setsDescanso = {}
        setsClase={}
        
        for estudio in self.EstudioIngresado:
            setsEstudio[estudio] = []
        for descanso in self.DescansoIngresado:
            setsDescanso[descanso]=[]
        for clase in self.ClaseIngresado:
            setsClase[clase]=[]
        setsEstudioKey = setsEstudio.keys()
        setsDescansoKey = setsDescanso.keys()
        setsClaseKey = setsClase.keys()
        
        for actividad in self.json_data:
            if actividad["Tiempo"]["numero semana"] == self.numeroSemana: #self.numeroSemana
                if actividad["Tipo Espec\u00edfico"]["Estudio"] != "":
                    self.setEstudio.append([actividad["Tipo Espec\u00edfico"]["Estudio"], actividad["Tiempo"]["Duracion"]])
                elif actividad["Tipo Espec\u00edfico"]["Clase"]!="":
                    self.setClase.append([actividad["Tipo Espec\u00edfico"]["Clase"], actividad["Tiempo"]["Duracion"]])


                elif actividad["Tipo Espec\u00edfico"]["descanso:"] != "":
                    self.setDescanso.append([actividad["Tipo Espec\u00edfico"]["descanso:"], actividad["Tiempo"]["Duracion"]])
        
        
       
        
        for par in self.setEstudio:
            for key in setsEstudioKey:
                if par[0] == key:
                    setsEstudio[key].append(par[1])
        for par in self.setClase:
            for key in setsClaseKey:
                if par[0] == key:
                    setsClase[key].append(par[1])
                    
        for par in self.setDescanso:
            for key in setsDescansoKey:
                if par[0] == key:
                    setsDescanso[key].append(par[1])
       
        print(setsDescanso)
        print(setsClase)        
        print(setsEstudio)
        for clase in setsClase:
            setsClase[clase]= sum(setsClase[clase])
        for estudio in setsEstudio:
            setsEstudio[estudio] = sum(setsEstudio[estudio])
        for descanso in setsDescanso:
            setsDescanso[descanso] = sum(setsDescanso[descanso])
       
        print("sumas:")
        print(setsDescanso)
        print(setsClase)
        print(setsEstudio)
        self.descansos= self.DescansoIngresado        
        self.tiemposDescanso = []
        self.tiemposEstudio = []
        self.tiemposClase = []
        for descanso in setsDescanso:
            self.tiemposDescanso.append(setsDescanso[descanso])
        for estudio in setsEstudio:
            self.tiemposEstudio.append(setsEstudio[estudio])
        for clase in setsClase:
            self.tiemposClase.append(setsClase[clase])
        print(self.tiemposDescanso)
        print(self.tiemposClase)
        print(self.tiemposEstudio)
        self.tiempoPorTipo = []
        self.tiempoSemanalDescansoTotalSuma = sum(self.tiemposDescanso)
        self.tiempoSemanalEstudioTotalSuma = sum(self.tiemposEstudio)
        self.tiempoSemanalClaseTotalSuma = sum(self.tiemposClase)
        self.tiempoPorTipo.append(self.tiempoSemanalDescansoTotalSuma)
        self.tiempoPorTipo.append(self.tiempoSemanalClaseTotalSuma)
        self.tiempoPorTipo.append(self.tiempoSemanalEstudioTotalSuma)
       
        self.clases = self.ClaseIngresado
        
        self.tipoActividadEspecifico = ["Descanso", "Clases", "Estudio"]
        self.actividadesDeEstudio = self.EstudioIngresado
        
        
        self.tiempoSemanalEstudioTotalSumaPromedioPorDia = round(self.tiempoSemanalEstudioTotalSuma/7,2)

        self.tiempoSemanalClaseTotalSumaPromedioPorDia = round(self.tiempoSemanalClaseTotalSuma/7,2)
        self.tiempoSemanalDescansoTotalSumaPromedioPorDia = round(self.tiempoSemanalDescansoTotalSuma/7,2)
        def minutosAHORA(minutos):
            horas = minutos/60
            rondeo = round(horas, 2)
            return rondeo
        self.ClaseEnHoras = minutosAHORA(self.tiempoSemanalClaseTotalSuma)    
        self.EstudioEnHoras = minutosAHORA(self.tiempoSemanalEstudioTotalSuma)
        self.DescansoEnHoras = minutosAHORA(self.tiempoSemanalDescansoTotalSuma) 
        print("en horas: "+ str(self.DescansoEnHoras ))
        print(str(self.tiempoSemanalEstudioTotalSumaPromedioPorDia))
        print(str(self.tiempoSemanalClaseTotalSumaPromedioPorDia))
        print(str(self.tiempoSemanalDescansoTotalSumaPromedioPorDia))
        
        
        
        
        self.llbTTAL = tk.Label(self.grafSemanaA,
                                text = "Tiempo utilizado en cada estudio de la semana pasada",
                                font=("Arial", 20) )
        self.fplot = Figure(figsize = (10,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.actividadesDeEstudio,self.tiemposEstudio,color = "c")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column = 0)
        self.llbTTAL.grid(row=0, column = 0)
        
        self.llbTTALL = tk.Label(self.grafSemanaA,
                                 text = "Tiempo utilizado en cada clase de la semana pasada" ,
                                font=("Arial", 20))
        self.fplot = Figure(figsize = (10,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.clases,self.tiemposClase,color = "r")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3, column = 0)
        self.llbTTALL.grid(row=2, column = 0)
        
        self.llbTTALLL = tk.Label(self.grafSemanaA,
                                  text = "Tiempo utilizado en cada descanso de la semana pasada",
                                font=("Arial", 20) )
        self.fplot = Figure(figsize = (10,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.descansos,self.tiemposDescanso,color = "g")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=5, column = 0)
        self.llbTTALLL.grid(row=4, column = 0)
        
        self.llbTTALLLL = tk.Label(self.grafSemanaA,
                                  text = "Tiempo utilizado en cada actividad de la semana pasada",
                                font=("Arial", 20) )
        self.fplot = Figure(figsize = (5,2), dpi=100)
        self.a = self.fplot.add_subplot(111).bar(self.tipoActividadEspecifico,self.tiempoPorTipo,color = "k")
        self.canvas = FigureCanvasTkAgg(self.fplot, self.grafSemanaA)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column = 1)
        self.llbTTALLLL.grid(row=0, column = 1)
        
        print("El promedio de estudio semanal es "+ str(self.tiempoSemanalEstudioTotalSumaPromedioPorDia))

        self.CanvasTabla = tk.Canvas(self.grafSemanaA)
        self.LabelStat1 = tk.Label(self.CanvasTabla,
                                   text = "Promedio (tEstudio/dia): ",
                                   font = ("arial", 17))
        self.LabelStat2 = tk.Label(self.CanvasTabla,
                                   text = "Promedio (tDescanso/dia): ",
                                   font = ("arial", 17))
        self.LabelStat3 = tk.Label(self.CanvasTabla,
                                   text = "Promedio (tClase/dia): ", 
                                   font = ("arial", 17))
        self.LabelStat1_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalEstudioTotalSumaPromedioPorDia)+" minutos",
                                     font = ("arial", 17))
        self.LabelStat2_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalClaseTotalSumaPromedioPorDia)+" minutos",
                                     font = ("arial", 17))
        self.LabelStat3_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalDescansoTotalSumaPromedioPorDia)+" minutos",
                                     font = ("arial", 17))
        self.LabelStat4 = tk.Label(self.CanvasTabla,
                                   text =  "Tiempo total de estudio: ",
                                   font = ("arial", 17))
        self.LabelStat5   =tk.Label(self.CanvasTabla,
                                    text =  "Tiempo total en clases: ",
                                    font = ("arial", 17))
        self.LabelStat6   = tk.Label(self.CanvasTabla,
                                     text =  "Tiempo total descansando: ",
                                     font = ("arial", 17))
        self.LabelStat4_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalEstudioTotalSuma)+ " minutos o " +str(self.EstudioEnHoras)+" horas",
                                     font = ("arial", 17))
        self.LabelStat5_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalClaseTotalSuma)+ " minutos o "+str(self.ClaseEnHoras)+" horas",
                                     font = ("arial", 17))
        self.LabelStat6_1 = tk.Label(self.CanvasTabla,
                                     text = str(self.tiempoSemanalDescansoTotalSuma)+ " minutos o "+str(self.DescansoEnHoras)+" horas",
                                     font = ("arial", 17))
        
        self.CanvasTabla.grid(row = 2, column =1, rowspan = 4)
        self.LabelStat1.grid(row = 0, column = 0)
        self.LabelStat2.grid(row= 1, column = 0)
        self.LabelStat3.grid(row = 2, column = 0)
        self.LabelStat1_1.grid(row = 0, column = 1)
        self.LabelStat2_1.grid(row = 1, column = 1)
        
        self.LabelStat3_1.grid(row = 2,column = 1)
        
        self.LabelStat4.grid(row = 3,column = 0)
        self.LabelStat5.grid(row = 4,column = 0)
        self.LabelStat6.grid(row = 5,column = 0)
        self.LabelStat4_1.grid(row = 3,column = 1)
        self.LabelStat5_1.grid(row = 4,column = 1)
        self.LabelStat6_1.grid(row = 5,column = 1)
        print(self.setEstudio)
        print(self.setClase)      
        print(self.setDescanso)    
    def vGrafDia(self):
        def GraphIt():
             #conjuntos
            self.setEstudio = []
            self.setClase = []
            self.setDescanso = []
            self.setTodos = []
             
             
            self.currentDT = datetime.datetime.now()
            self.diaSemana = self.currentDT.strftime("%A")
            print(self.diaSemana)
            #self.mes = self.currentDT.strftime("%B")
            print(self.mes)
            
            self.tiempoDiarioBruto = []
            self.defnirAct= []
            self.tiempoDiarioBrutoEstudio =[]
            self.tiempoDiarioBrutoClase =[]
            self.tiempoDiarioBrutoDescanso =[]
            self.actEstudio =[]
            self.actClase=[]
            self.actDescanso=[]
            

            self.json_data = []
            self.file = open(self.json_file, "r")
            for self.line in self.file:
            	self.json_line = js.loads(self.line)
            	self.json_data.append(self.json_line)
            
            self.file.close()

            
            conjuntoClase = {}
            conjuntoEstudio = {}
            conjuntoDescanso = {}
            conjuntoTodos = {}
            for actividad in self.json_data:
                if actividad["Tiempo"]["Fecha"] == self.fecha and actividad["Tiempo"]["mes"]==self.mes :
                    if actividad["Tipo Espec\u00edfico"]["Estudio"] != "":
                        self.defnirAct.append(actividad["Tipo Espec\u00edfico"]["Estudio"])
                        self.actEstudio.append(actividad["Tipo Espec\u00edfico"]["Estudio"])
                        self.tiempoDiarioBruto.append(actividad["Tiempo"]["Duracion"])
                        self.tiempoDiarioBrutoEstudio.append(actividad["Tiempo"]["Duracion"])
                        self.setEstudio.append([actividad["Tipo Espec\u00edfico"]["Estudio"],
                                               actividad["Tiempo"]["Duracion"]])
                        self.setTodos.append([actividad["Tipo Espec\u00edfico"]["Estudio"],
                                               actividad["Tiempo"]["Duracion"]])
                    elif actividad["Tipo Espec\u00edfico"]["Clase"]!="":
                        self.defnirAct.append(actividad["Tipo Espec\u00edfico"]["Clase"])
                        self.actClase.append(actividad["Tipo Espec\u00edfico"]["Clase"])
                        self.tiempoDiarioBruto.append(actividad["Tiempo"]["Duracion"])
                        self.tiempoDiarioBrutoClase.append(actividad["Tiempo"]["Duracion"])
                        self.setClase.append([actividad["Tipo Espec\u00edfico"]["Clase"],actividad["Tiempo"]["Duracion"]])
                        self.setTodos.append([actividad["Tipo Espec\u00edfico"]["Clase"],actividad["Tiempo"]["Duracion"]])
                    elif actividad["Tipo Espec\u00edfico"]["descanso:"] != "":
                        self.defnirAct.append(actividad["Tipo Espec\u00edfico"]["descanso:"])
                        self.actDescanso.append(actividad["Tipo Espec\u00edfico"]["descanso:"])
                        self.tiempoDiarioBruto.append(actividad["Tiempo"]["Duracion"])
                        self.tiempoDiarioBrutoDescanso.append(actividad["Tiempo"]["Duracion"])
                        self.setDescanso.append([actividad["Tipo Espec\u00edfico"]["descanso:"],
                                                actividad["Tiempo"]["Duracion"]])
                        self.setTodos.append([actividad["Tipo Espec\u00edfico"]["descanso:"],
                                                actividad["Tiempo"]["Duracion"]])                        
            print("actividades registradas:")
            print(self.defnirAct)
            print("el bruto:")
            print(self.tiempoDiarioBruto)
            self.tiempoDiarioBrutoEstudio
            self.tiempoDiarioBrutoClase
            self.tiempoDiarioBrutoDescanso
            self.tiempoDiarioBruto
            for actividad in self.defnirAct:
                conjuntoTodos[actividad] = []
            for descanso in self.actDescanso:
                conjuntoDescanso[descanso]=[]
            for estudio in self.actEstudio:
                conjuntoEstudio[estudio]=[]
            for clase in self.actClase:
                conjuntoClase[clase]=[]       
            
            conjuntoClaseKey = conjuntoClase.keys()
            conjuntoEstudioKey =conjuntoEstudio.keys()
            conjuntoDescansoKey = conjuntoDescanso.keys()
            conjuntoTodosKey = conjuntoTodos.keys()
            
            for par in self.setTodos:
                for key in conjuntoTodosKey:
                    if par[0] == key:
                        conjuntoTodos[key].append(par[1])                
            
            for par in self.setEstudio:
                for key in conjuntoEstudioKey:
                    if par[0] == key:
                        conjuntoEstudio[key].append(par[1])
            for par in self.setClase:
                for key in conjuntoClaseKey:
                    if par[0] == key:
                        conjuntoClase[key].append(par[1])            
            for par in self.setDescanso:
                for key in conjuntoDescansoKey:
                    if par[0] == key:
                        conjuntoDescanso[key].append(par[1])
            print("antes de sumar repetidos:")
            print(conjuntoEstudio)
            print(conjuntoClase)
            print(conjuntoDescanso)
            print(conjuntoTodos)
            for key in conjuntoTodos:
                conjuntoTodos[key] = sum(conjuntoTodos[key])
            for key in conjuntoEstudio:
                conjuntoEstudio[key] = sum(conjuntoEstudio[key])
            for key in conjuntoClase:
                conjuntoClase[key] = sum(conjuntoClase[key])
            for key in conjuntoDescanso:
                conjuntoDescanso[key] = sum(conjuntoDescanso[key])
            TiempoTodos= []
            TiempoEstudio= []
            TiempoClase= []
            TiempoDescanso = []
            for key in conjuntoTodos:
                TiempoTodos.append(conjuntoTodos[key])
            for key in conjuntoEstudio:
                TiempoEstudio.append(conjuntoEstudio[key])
            for key in conjuntoClase:
                TiempoClase.append(conjuntoClase[key]) 
            for key in conjuntoDescanso:
                TiempoDescanso.append(conjuntoDescanso[key])
            tiempoTipoEspecífico = []
            tiempoClaseSuma = sum(TiempoClase)
            tiempoTipoEspecífico.append(tiempoClaseSuma)
            tiempoDescansoSuma = sum(TiempoDescanso)
            tiempoTipoEspecífico.append(tiempoDescansoSuma)
            tiempoEstudioSuma = sum(TiempoEstudio)
            tiempoTipoEspecífico.append(tiempoEstudioSuma)
            
            
            
            print("luego de sumar repetidos.")
            print(conjuntoEstudio)
            print(conjuntoClase)
            print(conjuntoDescanso)
            
            tiposEspecíficos = ["Clase","Descaso","Estudio"]
            
            self.llbTTAL = tk.Label(self.vGrafDia, text = "Tiempo utilizado en cada tipo de actividad del "+ self.fecha+" de " +self.mes+"." )
            self.fplot = Figure(figsize = (5,2), dpi=100)
            self.a = self.fplot.add_subplot(111).bar(tiposEspecíficos,tiempoTipoEspecífico,color = "c")
            self.canvas = FigureCanvasTkAgg(self.fplot, self.vGrafDia)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=3, column = 2)
            self.llbTTAL.grid(row=2, column = 2)
            
            
            self.llbDesc = tk.Label(self.vGrafDia, text ="Tiempo utilizado en cada descanso del "+ self.fecha+" de " + self.mes+"."  )
            self.gplot = Figure(figsize = (5,2), dpi=100)
            self.g = self.gplot.add_subplot(111).bar(conjuntoDescansoKey,TiempoDescanso, color = "g")
            self.canvas = FigureCanvasTkAgg(self.gplot, self.vGrafDia)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=3, column = 0)
            self.llbDesc.grid(row= 2, column = 0)
            
            self.llbEst = tk.Label(self.vGrafDia, text = "Tiempo utilizado en cada estudio del "+ self.fecha+" de " +self.mes+".")
            self.hplot = Figure(figsize = (5,2), dpi=100)
            self.h = self.hplot.add_subplot(111).bar(conjuntoEstudioKey,TiempoEstudio, color = "r")
            self.canvas = FigureCanvasTkAgg(self.hplot, self.vGrafDia)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column = 1)
            self.llbEst.grid(row=0, column = 1)
            
            self.llbClas = tk.Label(self.vGrafDia, text = "Tiempo utilizado en cada clase del "+ self.fecha+" de " +self.mes+"." )
            self.jplot = Figure(figsize = (5,2), dpi=100)
            self.g = self.jplot.add_subplot(111).bar(conjuntoClaseKey,TiempoClase, color = "k")
            self.canvas = FigureCanvasTkAgg(self.jplot, self.vGrafDia)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=3, column = 1)
            self.llbClas.grid(row=2, column = 1)
            
            self.llbTIT = tk.Label(self.vGrafDia, text = "Tiempo utilizado en cada actividad del "+ self.fecha+" de " +self.mes+"." )
            self.kplot = Figure(figsize = (5,2), dpi=100)
            self.k = self.kplot.add_subplot(111).bar(conjuntoTodosKey,TiempoTodos,color="b")
            self.canvas = FigureCanvasTkAgg(self.kplot, self.vGrafDia)
            self.canvas.draw()
            self.canvas.get_tk_widget().grid(row=1, column = 2)
            self.llbTIT.grid(row=0, column = 2)
      
        def EntryDiaGet():
            global fecha
            global mes
            #self.fecha = tk.IntVar()
            self.fecha = self.EntryDia.get()
            self.mes = self.EntryMes.get()
            print("la fecha es "+self.fecha)
            print("el mes es "+ self.mes)
            GraphIt()
        
            return self.fecha, self.mes
        
        
       # self.fecha = self.currentDT.strftime("%d")
        
        self.vGrafDia = tk.Toplevel()
        self.vGrafDia.geometry("1500x500")
        
        self.json_file = "DATA.txt"
        self.CanvasEntry = tk.Canvas(self.vGrafDia)
        self.lblEntry = tk.Label(self.CanvasEntry,
                                 text = "Día a analizar",
                                 font = ("arial", 18))
        global EntryDia
        self.EntryDia = tk.Entry(self.CanvasEntry)
        self.btnEntry = tk.Button(self.CanvasEntry,
                                 text = "mostrar gráficos",
                                 font = ("arial", 18),
                                 command = EntryDiaGet)
        self.lblMes = tk.Label(self.CanvasEntry, 
                               text = "mes en inglés. ej: April",
                               font = ("arial", 18))
        self.EntryMes = tk.Entry(self.CanvasEntry)
        
       
       
        self.CanvasEntry.grid(column = 0, row = 0, rowspan = 2)
        self.lblEntry.grid(column = 0, row = 0)
        self.EntryDia.grid(column = 0, row = 1)
        self.lblMes.grid(column = 0, row = 2)
        self.EntryMes.grid(column = 0, row = 3)
        self.btnEntry.grid(column = 0, row = 4)   

        #obtiene fecha (numero de dia del mes) no hay que cambiarle el nombre a
        # la variable, pero hay que hacer que se pueda ingresar en el lado derecho
        #el numero de dia.
        
      
         
        
        
        
        
        """
        no los saco pq podrian ser utiles
        plt.figure(1)
        plt.bar(self.defnirAct, self.tiempoDiarioBruto, color="b", label="actividades registradas")
        plt.legend()
        plt.title("Tiempo utilizado en cada actividad del "+ self.fecha+" de " +self.mes+"." )
        plt.xlabel("Actividad")
        plt.ylabel("Tiempo")
        plt.figure(2)
        plt.bar(self.actEstudio, self.tiempoDiarioBrutoEstudio, color = "k", label= "estudio registrado")
        plt.legend()
        plt.title("Tiempo utilizado en cada estudio del "+ self.fecha+" de " +self.mes+"." )
        plt.xlabel("Asignaturas")
        plt.ylabel("Tiempo")
        plt.figure(3)
        plt.bar(self.actClase, self.tiempoDiarioBrutoClase, color = "r", label= "clases registradas")
        plt.legend()
        plt.title("Tiempo utilizado en cada clase del "+ self.fecha+" de " +self.mes+"." )
        plt.xlabel("Clase")
        plt.ylabel("Tiempo")
        plt.figure(4)
        
        plt.bar(self.actDescanso, self.tiempoDiarioBrutoDescanso, color = "g", label = "descanso registrado")
        plt.legend()
        plt.title("Tiempo utilizado en cada descanso del "+ self.fecha+" de " + self.mes+"." )
        plt.xlabel("Tipo Descanso")
        plt.ylabel("Tiempo")
        plt.figure(5)
        plt.bar(self.TuplaTipoActividad, self.TuplaTiempos, color = "c", label = "tiempo en cada tipo de actividad")
        plt.title("Tiempo utilizado en cada tipo de actividad del "+ self.fecha+" de " +self.mes+"." )
        plt.xlabel("Tipo Actividad")
        plt.ylabel("Tiempo")
        plt.show()
        """
           
        

        
    def vtimer(self):
        def showActivity():
            json_data = []
            self.EstudioIngresado =[]
            self.ClaseIngresado = []
            self.DescansoIngresado =[]
            with open('Actividades.txt', 'r') as file:
                for line in file:
                    json_line = js.loads(line)
                    json_data.append(json_line)
            for elemento in json_data:
                if elemento["Tipo"] == "Estudio":
                    self.EstudioIngresado = elemento["Actividades"]
                    print(self.EstudioIngresado)
                if elemento["Tipo"] == "Clase":
                    self.ClaseIngresado = elemento["Actividades"]
                    print(self.ClaseIngresado)
                if elemento["Tipo"] == "Descanso":
                    self.DescansoIngresado = elemento["Actividades"]
                    print(self.DescansoIngresado)
            return self.EstudioIngresado, self.ClaseIngresado,self.DescansoIngresado
        showActivity()
        
        self.asignaturasEstudio = self.EstudioIngresado
        self.vt = tk.Toplevel()
        self.vt.geometry("800x350")
        #global LblActividad 
        
        self.LblActividad = tk.Label(self.vt, 
                                     text="actividad: ",
                                     font=("Arial", 12))
        
        
        self.bvt1 = tk.Menubutton(self.vt,
                              text= "asignatura a estudiar",
                              width = 21,
                              height= 3,
                              font=("Arial", 12),
                              state = tk.DISABLED)
        self.bvt1.menu = tk.Menu(self.bvt1)
        self.bvt1["menu"] = self.bvt1.menu
        for estudio in self.asignaturasEstudio:
            self.bvt1.menu.add_command(label = estudio,
                                   command = partial(self.guardarTipoEstudio, estudio))
         
        self.TipoActividad = ["Estudio","Clase","Descanso"]
        self.b2vt1 =  tk.Menubutton(self.vt,
                              text= "tipo de actividad",
                              width = 21,
                              height= 3,
                              font=("Arial", 12))
        self.b2vt1.menu = tk.Menu(self.b2vt1)
        self.b2vt1["menu"]= self.b2vt1.menu
        self.b2vt1.menu.add_command(label= self.TipoActividad[0],
                                   command = lambda : self.LblTipoActividad.configure(text = "Tipo: {tipo}".format(tipo = self.TipoActividad[0],
                                   command = self.guardarTipoAtividad(self.TipoActividad[0]))))
        self.b2vt1.menu.add_command(label= self.TipoActividad[1],
                                   command = lambda : self.LblTipoActividad.configure(text = "Tipo: {tipo}".format(tipo = self.TipoActividad[1],
                                command = self.guardarTipoAtividad(self.TipoActividad[1]))))
        self.b2vt1.menu.add_command(label= self.TipoActividad[2],
                                   command = lambda : self.LblTipoActividad.configure(text = "Tipo: {tipo}".format(tipo = self.TipoActividad[2],
                                   command = self.guardarTipoAtividad(self.TipoActividad[2]))))
        
        
        self.clases = self.ClaseIngresado
        

        self.b3vt1 = tk.Menubutton(self.vt,
                                   text = "clase",
                                   width = 21, 
                                   height= 3,
                                   font=("Arial", 12),
                              state = tk.DISABLED)
        self.b3vt1.menu = tk.Menu(self.b3vt1)
        self.b3vt1["menu"]= self.b3vt1.menu
        for clase in self.clases:
            self.b3vt1.menu.add_command(label = clase,
                                   command = partial(self.guardarTipoClase, clase))
        
        self.TipoDescanso = self.DescansoIngresado
        self.b4vt1 = tk.Menubutton(self.vt, 
                                   text = "tipo descanso", 
                                   width = 21, 
                                   height= 3,
                                   font=("Arial", 12), state=tk.DISABLED )
        self.b4vt1.menu = tk.Menu(self.b4vt1)
        self.b4vt1["menu"]= self.b4vt1.menu
        for descanso in self.TipoDescanso:
            self.b4vt1.menu.add_command(label = descanso,
                                   command = partial(self.guardarTipoDescanso, descanso))
            
          
        self.LblMin = tk.Label(self.vt,
                               text = "Minutos",
                               font=("Arial", 12))
        global Entry1
        self.Entry1 = tk.Entry(self.vt)
        self.LblHr = tk.Label(self.vt,
                               text = "Horas",
                               font=("Arial", 12))
        global Entry2
        self.Entry2 = tk.Entry(self.vt)
        
        self.b5vt1 = tk.Button(self.vt, text = "Configurar Temporizador",
                               width = 21, 
                               height= 3,
                               font=("Arial", 12),  command = self.getterEntryTimer)
        self.b6vt1 = tk.Button(self.vt, text = "Iniciar Temporizador",
                               width = 21, 
                               height= 3,
                               command = self.countdown,
                               font=("Arial", 12))
        global LblTiempo
        self.LblTiempo = tk.Label(self.vt,
                                  text= "",
                                  font= ("Arial", 60))
        
        self.LblTipoActividad = tk.Label(self.vt,
                                         text= "tipo: ",
                                         width = 21, 
                                         height= 3,
                                         font=("Arial", 12)) 
        self.btnGuard = tk.Button(self.vt, text= "Guardar Datos",
                                  width = 15, 
                                  height= 3,
                                  command = self.guardarActividadEspecifica,
                                  font=("Arial", 12))
        self.btnPausa = tk.Button(self.vt,
                               width = 21, 
                               height= 3,
                               text = "Pausar/Continuar", command = self.estadoPausa, font=("Arial", 12))
        self.b2vt1.grid(column= 2, row=0)
        self.LblHr.grid(column = 0, row = 1)
        self.LblMin.grid(column = 0, row = 0)
        self.bvt1.grid(column=3, row=0)
        self.b5vt1.grid(column = 0, row = 2)
        self.Entry1.grid(column = 1, row = 0)
        self.Entry2.grid(column = 1, row=1)
        self.b3vt1.grid(column= 2, row=1)
        self.b4vt1.grid(column= 3, row=1)
        self.b6vt1.grid(column=1, row=2)
        self.LblTiempo.grid(column = 0, row= 4, columnspan=3)
        global LblTipoActividad
        global LblActividad
        
        self.LblTipoActividad.grid(column = 3, row = 2)
        self.LblActividad.grid(column = 3, row = 3)
        self.btnGuard.grid(column = 3, row = 4)
        self.btnPausa.grid(column = 2, row = 2)
     
    
    
    
    def guardarTipoAtividad(self, TActividad):
        self.TActividad = TActividad
        if self.TActividad == "Descanso":
            self.b4vt1['state'] = tk.NORMAL
            self.b3vt1['state'] = tk.DISABLED
            self.bvt1['state'] = tk.DISABLED

        if self.TActividad == "Estudio":
           self.bvt1['state'] = tk.NORMAL
           self.b4vt1['state'] = tk.DISABLED
           self.b3vt1['state'] = tk.DISABLED
        if self.TActividad == "Clase":
            self.b3vt1['state'] = tk.NORMAL
            self.b4vt1['state'] = tk.DISABLED
            self.bvt1['state'] = tk.DISABLED

            
        return TActividad
    

    def guardarTipoClase(self, TClase):
        self.TClase = TClase
        self.LblActividad.configure(text = "Actividad: {actividad}".format(actividad = self.TClase))
        return TClase
     
    def guardarTipoEstudio(self, TEstudio):
        self.TEstudio = TEstudio
        self.LblActividad.configure(text = "Actividad: {actividad}".format(actividad = self.TEstudio))
        return TEstudio
    def guardarTipoDescanso(self, TDescanso):
        self.TDescanso = TDescanso
        self.LblActividad.configure(text = "Actividad: {actividad}".format(actividad = self.TDescanso))
        return TDescanso
    
    def getterEntryTimer(self):
        self.minutos = int(self.Entry1.get())  # entry de minutos
        self.horas = int(self.Entry2.get())    # entry de segundos
        self.LblTiempo.configure(text="{hora}:{minuto}:{segundo}".format(hora =self.horas,
                                                                         minuto =self.minutos,
                                                                         segundo =self.segundos))
        
 
    def guardarActividadEspecifica(self):
        self.TipoActividadObtenido = self.TActividad
        self.TipoClaseObtenida = self.TClase
        self.TipoEstudioObtenido = self.TEstudio
        self.TipoDescansoObtenido = self.TDescanso

        def CheckerRepetidos(tipo,clase, descanso, estudio):
            if tipo == "Clase": 
                descanso = ""
                estudio = ""
                    
            if tipo == "Estudio":
                clase = ""
                descanso = ""
            if tipo =="Descanso":        
                estudio = ""
                clase = ""
            return [clase, descanso, estudio]
                
                
        self.sinRep = CheckerRepetidos(self.TipoActividadObtenido,self.TipoClaseObtenida, self.TipoDescansoObtenido,self.TipoEstudioObtenido)  
        self.mins = int(self.Entry1.get())
        self.hrs = int(self.Entry2.get())
        self.hrsEnMins = 60*self.hrs 
        self.duracion = self.mins + self.hrsEnMins
        self.currentDT = datetime.datetime.now()
        self.numeroSemana = self.currentDT.isocalendar()[1]
        print(self.numeroSemana)
        self.diaSemana = self.currentDT.strftime("%A")
        self.fecha = self.currentDT.strftime("%d")
        self.mes = self.currentDT.strftime("%B")
        js.data ={"Tipo Actividad": self.TActividad,
                  "Tipo Específico": {"Estudio":self.sinRep[2],
                                     "Clase":self.sinRep[0],
                                     "descanso:":self.sinRep[1]},
                  "Tiempo": {"Fecha":self.fecha,
                              "Duracion":self.duracion,
                              "dia semana":self.diaSemana,
                              "mes":self.mes,
                              "numero semana":self.numeroSemana}}
        self.guardado = open("DATA.txt", "a")  
        js.dump(js.data, self.guardado)
        self.guardado.write("\n")
        self.guardado.close()                                                                  
    
    
    def estadoPausa(self):
        if self.estado.get() == True:
            self.estado.set(False)
            print(self.estado.get())
            return self.estado
        if self.estado.get() == False:
            self.estado.set(True)
            print(self.estado.get())
            return self.estado
    def askEnPausa(self):
        return self.estado.get()
    
    def countdown(self):
        self.LblTiempo.after(1000, self.countdown)
        self.enPausa = self.askEnPausa()
        if self.segundos >0:
            self.LblTiempo.configure(text="{hora}:{minuto}:{segundo}".format(hora =self.horas,
                                                                         minuto =self.minutos,
                                                                         segundo =self.segundos))
            if self.enPausa == True:
                self.segundos -=0
            elif self.enPausa == False:
                self.segundos -=1 
        if self.segundos == 0:
            if self.minutos != 0:
                self.segundos = 59
                self.minutos -=1
                self.LblTiempo.configure(text="{hora}:{minuto}:{segundo}".format(hora =self.horas,
                                                                             minuto =self.minutos,
                                                                             segundo =self.segundos))
            else: 
                self.minutos = 0
        if self.minutos == 0:
            if self.horas != 0:
                self.horas -= 1
                self.minutos = 59
                self.LblTiempo.configure(text="{hora}:{minuto}:{segundo}".format(hora =self.horas,
                                                                             minuto =self.minutos,
                                                                           segundo =self.segundos))
            else: 
                self.horas = 0
                
        if self.horas == 0 and self.minutos == 0 and self.segundos ==0: 
            self.LblTiempo.configure(text= "¡Time's up!")
            os.startfile("household016.mp3")
            time.sleep(10)
            self.vt.destroy()

root = tk.Tk()

ventana1 = v1(root)
root.mainloop()
