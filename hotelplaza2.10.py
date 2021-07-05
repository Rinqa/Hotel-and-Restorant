from tkinter import*
from datetime import datetime
from tkinter import messagebox
#----------------------------------------------------------------------------------
#there are the primary root
#----------------------------------------------------------------------------------
qwert=Tk()
qwert.geometry("720x635+10-85")
qwert.title("J-Coders Academy")
qwert["bg"]="gray"
lista1=[]
lista2=[]
lista3=[]
lista4=''
cmimiiii=''
listaaaa={'Makiato e Madhe':0.5,'viski':5,'Mint Chocolate Chip':0.7,"Panzenella":2,"Urap":2.3,"Mish i bardh":3.0,"Acar":1.5,"Greek salad":2.0,"Larb":1.6,' Asian Sesame Chicken':2.0," Thai Soyabean":5.0,"Potato Salad":3.0,"Carrot Salad":2.0,'Salted Caramel Pretzel':2,'Coffee':0.5,'Raspberry Truffle':0.9,'Cookies & Cream':3,"Jack daniels":2.5,"Mango":0.5,'Ekspreso e Vogel':0.5,'Dredhez':1,'Pjeshk':1,'Cocacola':1,'Sprite':1,'Nescafe':0.5,'chapoqino':0.5,'Vishnje':1,'Molle':1,'Laqin':1,'RedBull':2.5,'Bambi':0.5,'Expreso':0.5,'Portokall':1,'Fruta mali':1,'Fanta':1,'Boze':1,'Hot Chocolate':1,'Qaj Mali':1,'Limonada':1,'Boronice':1,'Uje natyral':1,'Uje i gazuar':0.5,"Ve me Suxhuk":1.5,'Saundviq Pule':2,'chicken Burger':2.5,'Makarona':1.5,'Shapgeta':1.5,'Pasul':2,'Gullash':2.5,'Omlet me perime':2,'Trileqe':1,'Bakllava':1.5,'Bombic':0.7,'Raffelo':2.2,'Bounty':0.5,'Fruta Mali':1,'Kinder':1,'Keks Torte':1,'Trio':1,'Rocher':1,'Hamburger':1.7,'Tost':1,'HotDog':1,'Qebapa':1,'Sendviq':2,'Pomfrita':1.2,'Sendviq Agora':2.5,'Sallat greke':0.5,'sallat shope':0.5,'sallat mishpule':2,'sallat ruse':1,'sallat tuna':3,'sallat verore':0.5,'vanill':0.5,'lajthi':0.5,'karramel':0.5,'qokolade':0.5,'Dredhez':0.5,'fruta':0.5,'kivi':0.5,'RedBull':2.5}
t1=Text()
rez=''
lis1=['Rinor','Admin']
lis2=['rinqa','4321']
user=Entry()
Password=Entry(show="*")
#----------------------------------------------------------------------------------
#from there started the restorant window
#----------------------------------------------------------------------------------
def rootikryesor():
	#----------------------------------------------------------------------------------
	#the primary root on the restorant project
	#----------------------------------------------------------------------------------
	r=Toplevel()



	r.geometry('1366x768')
	r.title('caffe')


	def mbyllja(d):
		if(d=='Log out'):
			r.destroy()



	def faqja(x):

		#----------------------------------------------------------------------------------
		#secondary root on the restorant project
		#----------------------------------------------------------------------------------

		root=Toplevel(r)
		root.geometry('1366x768')
		root.title("J-Coders Academy")

		frm1=Frame(root,bg='#979599')
		frm1.place(x=0,y=0,width=1366,height=768)
		frm2=Frame(root,bg='#979599')
		frm2.place(x=150,y=0,width=1216,height=150)
		frm3=Frame(frm1,bg='#979599')
		frm3.place(x=300,y=150,width=1200,height=50)
		frm4=Frame(frm1,bg='#616665')
		frm4.place(x=0,y=708,width=1366,height=38)

		h=Label(frm1,text=('Tavolina nr:'+x),bg='#979599',font=('Imprint MT Shadow',17),fg='darkblue')
		h.place(x=0,y=0,width=150,height=50)
		ent=Label(frm1,text=1,bg='#979599',fg='darkBlue',font=('Imprint MT Shadow',25))
		ent.place(x=0,y=50,width=150,height=50)
		xpos=0
		ypos=0
		f=0

		def shfaq():
			global lista1
			global lista2
			global lista3
			global lista4
			global t1
			global rez
			t1=Text(frm1,bg='lightblue',fg='darkblue')
			rez='  ~/~ HOTEL J-Coders ~/~'+'\n'+"\t~Gjilan~"+"\n"+'     ~Tavolina nr:'+x+'~'+'\n'+'Produkti:'+'\t\t'+'  Saisia:'+'\t'+'  Qmimi:'+'\n'

			t1.place(x=0,y=150,height=558,width=300)
			cmimiiii=0.0

			for i in range(0,len(lista1)):
				rez=rez+lista1[i]+'\t\t\t'+str(lista2[i])+'\t'+str(lista3[i]*float(ent.cget('text')))+'\n'
				cmimiiii=cmimiiii+(float(lista2[i])*float(lista3[i]))
				ent.config(text=1)
			rez=rez+'Totali i fatures: \t\t\t\t '+str(cmimiiii)+'\n'+"TEL:\t\t     +383-045-638-783"+'\n'+"ADRESA:\t\t     Enver Miftari"+'\n	Ju Faleminderit '+'\n'+'-------------------------------------\n'
			t1.insert(INSERT,rez)

		#------------------------------------------------------------------------------------------
		#there we have defines the price of the product on bild where we use the dictonary function
		#------------------------------------------------------------------------------------------

		def cmimi(produkti):
			global lista3
			global listaaaa
			x=listaaaa.get(produkti)
			lista3.append(x)



			#----------------------------------------------------------------------------------
			#  d is the text of the button
			#there we have defines the bild
			#----------------------------------------------------------------------------------
		def tura(d):
			global lista1
			global lista2
			global lista3

			lista1.append(d)
			y=ent.cget('text')
			lista2.append(y)

			cmimi(d)
			shfaq()
		#----------------------------------------------------------------------------------
		#there we have make the quantity(sasia) of the product where see on the bild
		#and we made some function to delete,print and back to the primary root
		#----------------------------------------------------------------------------------
		def sasi(c):
			global lista1
			global lista2
			global lista3
			global rez
			global lista4
			global t1
			global cmimiiii
			if(c=="Mbrapa"):

				root.destroy()
				lista1=[]
				lista2=[]
				lista3=[]

			elif(c=='Fshije'):
				t1.delete(1.0,END)

				lista1=[]
				lista2=[]
				lista3=[]
			elif(c=='Faktura'):
				print(rez)

				lista4=lista4+rez
				file=open('rest.txt','a')
				file.write('\n'+lista4+"\n")



			elif(c=='1'):
				ent.config(text='1')
			elif(c=='2'):
				ent.config(text='2')
			elif(c=='3'):
				ent.config(text='3')
			elif(c=='4'):
				ent.config(text='4')
			elif(c=='5'):
				ent.config(text='5')
			elif(c=='6'):
				ent.config(text='6')
			elif(c=='7'):
				ent.config(text='7')
			elif(c=='8'):
				ent.config(text='8')
			elif(c=='9'):
				ent.config(text='9')
			elif(c=='10'):
				ent.config(text='10')
		#----------------------------------------------------------------------------------
		#personal data
		#----------------------------------------------------------------------------------
		frm4=Frame(frm1,bg='#616665')
		frm4.place(x=0,y=708,width=1366,height=38)
		lb1=Label(frm4,text='© Copyright by:Rinor Biqku  tel:045-638-783 E-mail:r.biqku342@gmail.com  Gjilan',bg='#616665',font=('Imprint MT Shadow',15),fg='darkblue')
		lb1.place(x=30,y=0)
		frm5=Frame(frm1,bg='#979599')
		frm5.place(x=300,y=200,width=1306,height=500)
		def zgjellja(x):
			global fm1
			global fm2
			global fm3
			global fm4
			global fm5
			if(x=='pijet'):
				fm1=Frame(frm1,bg='#979599')
				fm1.place(x=300,y=200,width=1306,height=500)
				p=['Makiato e Madhe','Ekspreso e Vogel','Dredhez','Pjeshk','Cocacola','Sprite','Nescafe','chapoqino','Vishnje','Molle','Laqin','RedBull','Bambi','Expreso','Portokall','Fruta mali','Fanta','Boze','Hot Chocolate','Qaj Mali','Limonada','Boronice','Uje natyral','Uje i gazuar',"viski","Jack daniels"]
				xpos=0
				ypos=5
				t=0
				for i in range(0,len(p)):
					b=Button(fm1,text=p[i],bg='orange',font=('Arial',12),fg='darkblue')
					b.place(x=xpos,y=ypos,width=130,height=50)
					t=t+1
					if(t==7):
						t=0
						xpos=0
						ypos=ypos+55
					else:
						xpos=xpos+140
					b.config(command=lambda d=b.cget('text'):tura(d))

			elif(x=='ushqimet'):
				fm3=Frame(frm1,bg='#979599')
				fm3.place(x=300,y=200,width=1306,height=500)
				t=0
				xpos=0
				ypos=5

				ush=["Ve me Suxhuk",'Saundviq Pule','chicken Burger','Makarona','Shapgeta','Pasul','Gullash','Omlet me perime']
				for i in range(0,len(ush)):
					n=Button(fm3,text=ush[i],bg='lightgreen',fg='darkblue')
					n.place(x=xpos,y=ypos,width=130,height=50)
					t=t+1
					if(t==7):
						t=0
						xpos=0
						ypos=ypos+55
					else:
						xpos=xpos+135
					n.config(command=lambda d=n.cget('text'):tura(d))


			elif(x=='Embelsira'):
				fm2=Frame(frm1,bg='#979599')
				fm2.place(x=300,y=200,width=1306,height=500)
				t=0
				xpos=0
				ypos=5
				em=['Trileqe','Bakllava','Bombic','Raffelo','Bounty','Fruta Mali','Kinder','Keks Torte','Trio','Rocher']
				for i in range(0,len(em)):
					p=Button(fm2,text=em[i],bg='#f2f458',fg='darkblue')
					p.place(x=xpos,y=ypos,width=130,height=50)
					t=t+1
					if(t==7):
						t=0
						xpos=0
						ypos=ypos+55
					else:
						xpos=xpos+135
					p.config(command=lambda d=p.cget('text'):tura(d))


			elif(x=='Fast Food'):
				fm4=Frame(frm1,bg='#979599')
				fm4.place(x=300,y=200,width=1306,height=500)
				xpos=0
				ypos=5
				t=0
				s=['Hamburger','Tost','HotDog','Qebapa','Sendviq','Pomfrita','Sendviq Agora','Mish i bardh']
				for i in range(0,len(s)):
					l=Button(fm4,bg='#e8cc86',text=s[i],fg='darkblue')
					l.place(x=xpos,y=ypos,width=130,height=50)
					t=t+1
					if(t==7):
						t=0
						xpos=0
						ypos=ypos+55
					else:
						xpos=xpos+135
					l.config(command=lambda d=l.cget('text'):tura(d))

			elif(x=='sallatat'):
				fm5=Frame(frm1,bg='#979599')
				fm5.place(x=300,y=200,width=1306,height=500)
				xpos=0
				ypos=5
				t=0
				a=['Sallat greke','sallat shope',"Acar","Greek salad",'sallat mishpule',"Larb","Urap",'sallat ruse',"Carrot Salad",'sallat tuna','sallat verore','Panzenella'," Asian Sesame Chicken"," Thai Soyabean"]
				for i in range(0,len(a)):
					bn=Button(fm5,bg='green',text=a[i],fg='white')
					bn.place(x=xpos,y=ypos,width=130,height=50)
					t=t+1

					if(t==7):
						t=0
						xpos=0
						ypos=ypos+55
					else:
						xpos=xpos+135
					bn.config(command=lambda d=bn.cget('text'):tura(d))

			elif(x=='Akullore'):
				fm6=Frame(frm1,bg='#979599')
				fm6.place(x=300,y=200,width=1306,height=500)
				xpos=0
				ypos=5
				t=0
				c=['vanill','lajthi','karramel','qokolade','Dredhez','fruta','kivi','RedBull','Cookies & Cream','Mint Chocolate Chip',"Mango",'Salted Caramel Pretzel','Coffee','Raspberry Truffle']
				for i in range(0,len(c)):
					bn=Button(fm6,bg='#9befe5',text=c[i],fg='darkblue')
					bn.place(x=xpos,y=ypos,width=130,height=50)
					t=t+1

					if(t==7):
						t=0
						xpos=0
						ypos=ypos+55
					else:
						xpos=xpos+135
					bn.config(command=lambda d=bn.cget('text'):tura(d))





		xpos=0
		ypos=10
		cnt=0
		y=['Sasia','1','2','3','4','5','Fshije','Faktura','Totali','6','7','8','9','10','Mbrapa']
		xpos=10
		ypos=0
		cnt=0
		for i in range(0,len(y)):
			n=Button(frm2,text=y[i],bg='lightgreen',font=('Algerian',20),fg='darkblue')
			n.place(x=xpos,y=ypos,width=140,height=70)
			cnt=cnt+1
			if(cnt==8):
				cnt=0
				xpos=10
				ypos=ypos+80
			else:
				xpos=xpos+150
			n.config(command=lambda c=n.cget('text'):sasi(c))
			if(y[i]=='Sasia'):
				n.config(bg='green',fg='lightBlue')
			elif(y[i]=='Totali'):
				n.config(bg='green',fg='lightBlue')
			elif(y[i]=='Faktura'):
				n.config(bg='green',fg='white')
				n.place(height=150,width=140)
			elif(y[i]=='Fshije'):
				n.config(bg='red',fg='black')
			elif(y[i]=='Mbrapa'):
				n.config(bg='darkgreen',fg='white')
		xpos=0
		ypos=5
		cnt=0
		e=['pijet','Akullore','sallatat','ushqimet','Fast Food','Embelsira','fruta deti']
		for i in range(0,len(e)):
			bnt=Button(frm3,bg='#a0ed61',text=e[i],font=('Algerian',15),fg='darkBlue')
			bnt.place(x=xpos,y=ypos,width=150,height=50)
			cnt=cnt+1
			if(cnt==6):
				cnt=0
				xpos=0
				ypos=ypos+50
			else:
				xpos=xpos+165
			bnt.config(command=lambda x=bnt.cget('text'):zgjellja(x))

	#----------------------------------------------------------------------------------
	#   on this place we make a place to joint the resotrant menager with his user name or
	#   or password on this he can see the printin bild on a day
	#----------------------------------------------------------------------------------

	#----------------------------------------------------------------------------------
	#background
	#----------------------------------------------------------------------------------
	fr1=Frame(r,bg='#979599')
	fr1.place(x=0,y=0,width=1366,height=768)
	fr2=Frame(fr1,bg="#979599")
	fr2.place(x=0,y=0,width=150,height=150)
	frm4=Frame(fr1,bg='#616665')
	frm4.place(x=0,y=708,width=1366,height=38)
	lbl = Label(frm4, bg='#616665',text='© Copyright by:Rinor Biqku  tel:045-638-783 E-mail:r.biqku342@gmail.com  Gjilan',
					font=('Castellar', 14), fg='lightblue')
	lbl.place(x=150, y=0)



	#----------------------------------------------------------------------------------
	#there we append the logo of the restorant in the primary root
	#----------------------------------------------------------------------------------
	

	#the restorant data

	l2=Label(fr1,text='J-Coders Academy',font=('Algerian',55),bg='#979599',fg='lightblue')
	l2.place(x=100,y=0,width=1216,height=100)
	logo=PhotoImage(file='J-C.png')
	l1=Label(l2,image=logo,bg="#979599")
	l1.place(x=90,y=-30,width=150,height=150)
	#----------------------------------------------------------------------------------
	# there are the dynamic button of the table of the restorant on the primary root

	#----------------------------------------------------------------------------------
	l=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63']
	xpos=50
	ypos=154
	cnt=0
	for i in range(0,63):
		btn=Button(fr1,text=l[i],bg='#767777',font=('Algerian',20),fg='lightblue')
		btn.place(x=xpos,y=ypos,width=50,height=50)
		cnt=cnt+1
		if(cnt==9):
			cnt=0
			xpos=50
			ypos=ypos+80
		else:
			xpos=xpos+150

		btn.config(command=lambda x=btn.cget('text'):faqja(x))

	h=Button(r,text='Log out',bg='#979599',fg='black')
	h.place(x=1234,y=10,width=100,height=30)
	h.config(command=lambda d=h.cget('text'):mbyllja(d))


	#----------------------------------------------------------------------------------
	# there we made the data and time:
	#----------------------------------------------------------------------------------
	def koha():
		#data dhe ora
		now=datetime.now()
		dita=now.day
		now=datetime.now()
		muaji=now.month
		now=datetime.now()
		viti=now.year
		now=datetime.now()
		ora=now.hour
		now=datetime.now()
		minuta=now.minute
		now=datetime.now()
		sekonda=now.second
		l1=Label(r,text=str(dita) + str(':'),bg='#979599',fg='black')
		l1.place(x=1280,y=50)
		l2=Label(r,text=str(muaji)+str(':'),bg='#979599',fg='black')
		l2.place(x=1300,y=50)
		l3=Label(r,text=str(viti),bg='#979599',fg='black')
		l3.place(x=1320,y=50)
		l4=Label(r,text=str(ora)+str(':'),bg='#979599',fg='black')
		l4.place(x=1280,y=70)
		l5=Label(r,text=str(minuta)+str("':"),bg='#979599',fg='black')
		l5.place(x=1299,y=70)
		l6=Label(r,text=str(sekonda)+str('"'),bg='#979599',fg='black')
		l6.place(x=1320,y=70)
		l7=Label(r,text='Date:',bg='#979599',fg='black')
		l7.place(x=1230,y=50)
		l8=Label(r,text='Time:',bg='#979599',fg='black')
		l8.place(x=1230,y=70)
		r.after(1000,koha)

	koha()
	r.mainloop()
#----------------------------------------------------------------------------------
# second root for there start the hotel app
#----------------------------------------------------------------------------------
def rootidyte():
	#----------------------------------------------------------------------------------
	# the primary root in the hotel app
	#----------------------------------------------------------------------------------
	root=Toplevel()
	root.geometry('700x400')
	root.config(bg='lightblue')
	root.title('J-Coders')
	lbl=Label(root,text='J-Coders',font=("Times",24,'italic'),bg='lightblue')
	lbl.place(x=93,y=15)
	img=PhotoImage(file ='JC.png')
	lbl2=Label(root,image=img,bg='lightblue')
	lbl2.place(x=50,y=70,width=300,height=250)
	xpos=380
	ypos=50
	cnt=0
	btn=[]
	te_dhenat=[]
	frm4=Frame(root,bg='lightblue')
	frm4.place(x=0,y=372,width=700,height=28)
	lb1=Label(frm4,text='© Copyright by:Rinor Biqku  tel:045-638-783 E-mail:r.biqku342@gmail.com  Gjilan',bg='lightblue',font=('Imprint MT Shadow',13),fg='darkblue')
	lb1.place(x=0,y=0)
	#----------------------------------------------------------------------------------
	#defines a root to destory
	#----------------------------------------------------------------------------------
	def mbyll():
	    	root.destroy()

	butoni=Button(root,text='Mbyll',font=('Arial',18),command=mbyll,bg='pink')
	butoni.place(x=10,y=320)
	#lista e kuzhinave
	listakuzh=['kitchen.png','kitchen2.png','kitchen3.png','kitchen4.png','kitchen5.png','kitchen.png','kitchen2.png','kitchen3.png','kitchen4.png','kitchen5.png','kitchen.png','kitchen2.png','kitchen3.png','kitchen4.png','kitchen5.png','kitchen.png','kitchen2.png','kitchen3.png','kitchen4.png','kitchen5.png']
	#lista e salloneve
	listasall=['salloni.png','salloni2.png','salloni3.png','salloni4.png','salloni5.png','salloni.png','salloni2.png','salloni3.png','salloni4.png','salloni5.png','salloni.png','salloni2.png','salloni3.png','salloni4.png','salloni5.png','salloni.png','salloni2.png','salloni3.png','salloni4.png','salloni5.png']
	#lista e banjove
	listabanjo=['banjo.png','banjo2.png','banjo3.png','banjo4.png','banjo5.png','banjo.png','banjo2.png','banjo3.png','banjo4.png','banjo5.png','banjo.png','banjo2.png','banjo3.png','banjo4.png','banjo5.png','banjo.png','banjo2.png','banjo3.png','banjo4.png','banjo5.png']
	#lista e dhomave te gjumit
	listagjum=['dhoma1.png','dhoma2.png','dhoma3.png','dhoma4.png','dhoma5.png','dhoma1.png','dhoma2.png','dhoma3.png','dhoma4.png','dhoma5.png','dhoma1.png','dhoma2.png','dhoma3.png','dhoma4.png','dhoma5.png','dhoma1.png','dhoma2.png','dhoma3.png','dhoma4.png','dhoma5.png',]
	gpozita=0
	#----------------------------------------------------------------------------------
	#map positon with a photo
	#----------------------------------------------------------------------------------
	def koordinatat():
	    window=Toplevel()
	    window.title('Hotel Plaza-Vendndodhja')
	    img2=PhotoImage(file='rruga.png')
	    lbl3=Label(window,image=img2)
	    lbl3.pack()

	    window.mainloop()
	btn21=Button(root,text='Shikoni ku gjendemi',font=('Times',18),command=koordinatat,bg='white')
	btn21.place(x=260,y=320)


	def ndrro(pozita):
	    global gpozita
	    gpozita=pozita
	    root2=Tk()
	    root2.geometry('950x650')
	    root2.title('Hotel Plaza-Faqja e dyte')
	    text=Text(root2,bg='lightblue',font=('Arial',14))
	    text.insert(INSERT,'Te dhenat e dhomes:' +  '\n' +
	        'Dhomat: 4 dhoma' + '\n' + '1 dhome gjumi' + '\n' + '1 Kuzhine' + '\n' + '1 banjo' + '\n' + '1 sallon'
	         + '\n' + 'Vendndodhja: Gjilan' +'\n' + "Ruga: Avdullah Tahiri" + '\n' )
	    text.place(x=560,y=240,width=350,height=280)
	    def mbrapa():
	    	root2.destroy()

	    btn22=Button(root2,text='<<<',font=('Arial',18),command=mbrapa,bg='lightblue')
	    btn22.place(x=0,y=603)
	    frm4=Frame(root2,bg='#616665')
	    frm4.place(x=63,y=622,width=1000,height=28)
	    lb1=Label(frm4,text='© Copyright by:Rinor Biqku  tel:045-638-783 E-mail:r.biqku342@gmail.com  Gjilan',bg='#616665',font=('Imprint MT Shadow',13),fg='darkblue')
	    lb1.place(x=0,y=0)

	#fotot e dhomave
	    def salloni():
	        nwin = Toplevel()
	        nwin.title("Salloni")
	        photo2 = PhotoImage(file = listasall[pozita-1])
	        lbl2 = Label(nwin, image = photo2)
	        lbl2.pack()
	        def mbrapa():
	    	    nwin.destroy()

	        btn22=Button(nwin,text='<<<',font=('Arial',18),command=mbrapa,bg='lightblue')
	        btn22.place(x=0,y=0)
	        nwin.mainloop()
	    def banjo():
	        nwin2 = Toplevel()
	        nwin2.title("Banjo")
	        photo2 = PhotoImage(file = listabanjo[pozita-1])
	        lbl2 = Label(nwin2, image = photo2)
	        lbl2.pack()
	        def mbrapa():
	    	    nwin2.destroy()

	        btn22=Button(nwin2,text='<<<',font=('Arial',18),command=mbrapa,bg='lightblue')
	        btn22.place(x=0,y=0)
	        nwin2.mainloop()
	    def kuzhina():
	        global gpozita
	        global listafoto
	        nwin3 = Toplevel()
	        nwin3.title("Kuzhina")
	        photo2 = PhotoImage(file = listakuzh[pozita-1])
	        lbl2 = Label(nwin3, image = photo2)
	        lbl2.pack()
	        def mbrapa():
	    	    nwin3.destroy()

	        btn22=Button(nwin3,text='<<<',font=('Arial',18),command=mbrapa,bg='lightblue')
	        btn22.place(x=0,y=0)
	        nwin3.mainloop()
	    def gjumi():
	        nwin4 = Toplevel()
	        nwin4.title("Dhoma e gjumit")
	        photo2 = PhotoImage(file = listagjum[pozita-1])
	        lbl2 = Label(nwin4, image = photo2)
	        lbl2.pack()
	        def mbrapa():
	    	    nwin4.destroy()

	        btn22=Button(nwin4,text='<<<',font=('Arial',18),command=mbrapa,bg='lightblue')
	        btn22.place(x=0,y=0)
	        nwin4.mainloop()

	     #labelat
	    l1=Label(root2,text='Emri',font=('Arial',17))
	    l1.place(x=530,y=20)
	    l2=Label(root2,text='Mbiemri',font=('Arial',17))
	    l2.place(x=530,y=60)
	    l3=Label(root2,text='Ditët',font=('Arial',17))
	    l3.place(x=530,y=100)
	    #hapsirat ku shkruhet emri
	    e1=Entry(root2,bg='lightblue',font=('Arial',15))
	    e1.place(x=630,y=20,width=170,height=30)
	    e2=Entry(root2,bg='lightblue',font=('Arial',15))
	    e2.place(x=630,y=60,width=170,height=30)
	    e3=Entry(root2,bg='lightblue',font=('Arial',15))
	    e3.place(x=630,y=100,width=170,height=30)


	    def merr():
	    	butoni1.config(state='normal')
	    	butoni2.config(state='normal')
	    	butoni3.config(state='normal')
	    	rezultatet=''
	    	e=e1.get()
	    	m=e2.get()
	    	d=e3.get()
	    	rezultatet='Emri:'+ e +'\n' + 'Mbiemri:' + m + '\n' + 'Ditët: '+ d + " ditë" + '\n'
	    	text.insert(INSERT,rezultatet)
	    	te_dhenat.append(e)
	    	te_dhenat.append(m)
	    	te_dhenat.append(d)
	    	txt=open('hotel.txt','a')
	    	txt.write('Emri: '+ e +'\n')
	    	txt.write('Mbiemri: '+ m + '\n')
	    	txt.write('Ditët: '+ d + " ditë" + '\n')
	    	txt.write('Dhoma: ' + lista[gpozita] + '\n')
	    	txt.close()
	    #butoni per marrjen e te dhenave
	    b5=Button(root2,text='Submit',font=('Arial',15),bg='lightblue',command=merr)
	    b5.place(x=830,y=30)
	    #butonat e dhomave
	    b1=Button(root2,text='Salloni',bg='#c1d3dd',font=("Times",20),command=salloni)
	    b1.place(x=20,y=20,width=500,height=500)
	    b2=Button(root2,text='Banjo',bg='#bfb8db',font=("Times",20),command=banjo)
	    b2.place(x=20,y=20,width=200,height=150)
	    b3=Button(root2,text='Kuzhina',bg='#bdff91',font=("Times",20),command=kuzhina)
	    b3.place(x=20,y=370,width=230,height=150)
	    b4=Button(root2,text='Dhoma e gjumit',bg='#fcbaba',font=("Times",20),command=gjumi)
	    b4.place(x=320,y=170,width=200,height=350)
	#funksioni per rezervim/regjistrimsb
	    def rezervo():
	    	global gpozita
	    	root2.destroy()
	    	btnlista[pozita].config(text='✓',font=('Arial',20))
	#funksioni per cregjistrim
	    def dil():
	        global gpozita
	        root2.destroy()
	        btnlista[pozita].config(text=lista[pozita],font=('Arial',15))

	    #butoni per rezervimin/regjistrim  e dhomes
	    b6=Button(root2,text='Rezervoni/Check in',bg='lightgreen',font=("Times",18),command=rezervo,state='disable')
	    b6.place(x=560,y=175)
	    b7=Button(root2,text='Check out',bg='lightgreen',font=("Times",18),command=dil)
	    b7.place(x=790,y=175)

	    #funksionat per pansion
	    def me_pansion():
	    	d=e3.get()
	    	totali=70
	    	butoni1.config(state='disable')
	    	butoni2.config(state='disable')
	    	butoni3.config(state='disable')
	    	b6.config(state='normal')
	    	b7.config(state='normal')
	    	text.delete("12.0" + '\n',END)
	    	text.insert(INSERT,'\n' + 'Pagesa: 70€ me pansion te plote' + '\n')
	    	txt=open('redoni2.txt','a')
	    	txt.write('Pagesa: ' + '70€ per dite' + '\n')
	    	txt.write('Totali: ' + str(totali*int(d)) + "€" + '\n' + '______________________________' + '\n')
	    	txt.close()
	    	butoni4.place(x=830,y=110)
	    	butoni5.place(x=830,y=110)
	    	butoni5.place_forget()
	    def gjysem():
	    	d=e3.get()
	    	totali=40
	    	butoni1.config(state='disable')
	    	butoni2.config(state='disable')
	    	butoni3.config(state='disable')
	    	b6.config(state='normal')
	    	b7.config(state='normal')
	    	text.delete("12.0" + '\n',END)
	    	text.insert(INSERT,'\n' + 'Pagesa: 40€ me gjysem pansion')
	    	txt=open('redoni2.txt','a')
	    	txt.write('Pagesa: ' + '40€ per dite' + '\n')
	    	txt.write('Totali: ' + str(totali*int(d)) + "€" + '\n' + '______________________________' + '\n')
	    	txt.close()
	    	butoni4.place(x=830,y=110)
	    	butoni4.place_forget()
	    	butoni5.place(x=830,y=110)
	    def pa_pansion():
	    	d=e3.get()
	    	totali=40
	    	butoni1.config(state='disable')
	    	butoni2.config(state='disable')
	    	butoni3.config(state='disable')
	    	b6.config(state='normal')
	    	b7.config(state='normal')
	    	text.delete("12.0" + '\n',END)
	    	text.insert(INSERT,'\n' + 'Pagesa: 25€ pa pansion')
	    	txt=open('redoni2.txt','a')
	    	txt.write('Pagesa: ' + '25€ per dite' + '\n')
	    	txt.write('Totali: ' + str(totali*int(d)) + "€" + '\n'  + '______________________________' + '\n')
	    	txt.close()
	    	butoni4.place(x=830,y=110)
	    	butoni4.place_forget()
	    	butoni5.place(x=830,y=110)
	    	butoni5.place_forget()

	    #butonat per pansion
	    butoni1=Button(root2,text='Pansion i plote - 70€',bg='lightgreen',font=("Times",23),command=me_pansion,state='disable')
	    butoni1.place(x=30,y=540)
	    butoni2=Button(root2,text='Me gjysem pansion - 40€',bg='lightgreen',font=("Times",23),command=gjysem,state='disable')
	    butoni2.place(x=330,y=540)
	    butoni3=Button(root2,text='Pa pansion - 25€',bg='lightgreen',font=("Times",23),command=pa_pansion,state='disable')
	    butoni3.place(x=680,y=540)

	    #funksioni per menu
	    def menu():
	        win = Toplevel()
	        win.title("Menu tërë ditore")
	        foto=PhotoImage(file='menu.png')
	        labela_per_menu=Label(win,image=foto)
	        labela_per_menu.pack()
	        win.mainloop()
	    butoni4=Button(root2,text='Menu',bg='lightgreen',font=("Times",18),command=menu)

	    def menu2():
	        window= Toplevel()
	        window.title("Mengjesi")
	        foto2=PhotoImage(file='menu2.png')
	        labela_per_menu2=Label(window,image=foto2)
	        labela_per_menu2.pack()
	        window.mainloop()
	    butoni5=Button(root2,text='Menu',bg='lightgreen',font=("Times",18),command=menu2)



	    root2.mainloop()
	def koha():
		#data dhe ora
		now=datetime.now()
		dita=now.day
		now=datetime.now()
		muaji=now.month
		now=datetime.now()
		viti=now.year
		now=datetime.now()
		ora=now.hour
		now=datetime.now()
		minuta=now.minute
		now=datetime.now()
		sekonda=now.second
		l1=Label(root,text=str(dita) + str(':'),bg='lightblue',fg='black')
		l1.place(x=410,y=20)
		l2=Label(root,text=str(muaji)+str(':'),bg='lightblue',fg='black')
		l2.place(x=430,y=20)
		l3=Label(root,text=str(viti),bg='lightblue',fg='black')
		l3.place(x=445,y=20)
		l4=Label(root,text=str(ora)+str(':'),bg='lightblue',fg='black')
		l4.place(x=536,y=20)
		l5=Label(root,text=str(minuta)+str(":"),bg='lightblue',fg='black')
		l5.place(x=555,y=20)
		l6=Label(root,text=str(sekonda)+str(''),bg='lightblue',fg='black')
		l6.place(x=575,y=20)
		l7=Label(root,text='Date:',bg='lightblue',fg='black')
		l7.place(x=380,y=20)
		l8=Label(root,text='Time:',bg='lightblue',fg='black')
		l8.place(x=500,y=20)
		root.after(1000,koha)

	koha()
	def klientat():
	    global txt
	    from os import startfile
	    startfile("C:\\Users\\blacksn0w\\Desktop\\hotel plaza 2.2\\hoteli2.10\\redoni2.txt")

	butonipertekst=Button(root,text='Klientat',bg='lightgreen',font=("Times",18),command=klientat)
	butonipertekst.place(x=560,y=318)


	btnlista=[]
	lista=['1A','1B','2A','2B','3A','3B','4A','4B','5A','5B','6A','6B','7A','7B','8A','8B','9A','9B','10A','10B']

	for i in range(0,len(lista)):
	    btn=Button(root,bg='#d7dae0',text=lista[i],font=('Arial',15))
	    btn.place(x=xpos,y=ypos,width=60,height=35)
	    btn.config(command=lambda e=i:ndrro(e))
	    btnlista.append(btn)
	    cnt=cnt+1
	    if(cnt==4):
	        cnt=0
	        xpos=380
	        ypos=ypos+50
	    else:
	        xpos=xpos+70
	root.mainloop()

#----------------------------------------------------------------------------------
#on this we make the place to log in form with dynamic button and a label.
#----------------------------------------------------------------------------------
en=Label(qwert,font=('Segoe Script',16),bg='gray',fg='white',text="Write your code!")
en.place(x=20,y=300,width=210,height=30)

L=['7','8','9','4','5','6','1','2','3','0','Fshije']
xpos=20
ypos=332
cnt=0
jasht=''
ylli=''

def click(vlera):
	global jasht
	jasht=jasht+vlera
	global ylli
	ylli=ylli+'*'
	en.config(text=ylli)


	if(vlera=='Fshije'):
		jasht=''
		en.config(text=jasht)
		ylli=''





for i in range(0,11):
	numrat=Button(qwert,text=L[i],bd=1,font=('Arial',15),bg='gray',fg="white")
	numrat.place(x=xpos,y=ypos,width=68,height=68)
	cnt=cnt+1
	if(cnt==3):
		cnt=0
		xpos=20
		ypos=ypos+70
	else:
		xpos=xpos+70
	numrat.config(command=lambda x=numrat.cget('text'):click(x))
	if(L[i]=="0"):
		numrat.place(width=138)
	elif(L[i]=="Fshije"):
		numrat.place(x=160)
#----------------------------------------------------------------------------------
#this is the login form on the first window
#----------------------------------------------------------------------------------
def loginii():
	global jasht
	global ylli
	if(jasht=="1234"):
		jasht=''
		ylli=''
		en.config(text="Write your code!")

		rootikryesor()


	elif(jasht=="4321"):
		jasht=''
		ylli=''
		en.config(text="Write your code!")
		rootidyte()

	else:
		messagebox.showerror("Error", "kodi i shënuar është i gabuar")
#--------------------------------------------------------------------------------------
#This is the windows 3,This window can open only the menager with his user and password
#---------------------------------------------------------------------------------------
def root3():
	global lista4
	global rez
	full=Toplevel()
	full.geometry("250x250+750+10")
	global lis1
	global lis2
	global user
	global Password

	full.title('Kyqja')
	user=Entry(full)
	user.place(x=120,y=10,width=100,height=20)
	Password=Entry(full,show="*")
	Password.place(x=120,y=50,width=100,height=20)
	def po():
		global user
		global Password
		x=user.get()

		y=Password.get()

		for i in range(0,len(lis1)):

			if(x==lis1[i]):
				if(y==lis2[i]):
					global lista1
					global lista2
					global lista3
					global lista4
					global rez
					global cmimiiii
					global rezultatet
					f=Toplevel(full)
					f.geometry('1366x768')
					f.title("Menager")
					file2=open("rest.txt","r")
					lexo1=file2.read()
					t2=Text(f,bg='lightblue')

					t2.place(x=0,y=0,height=768,width=683)
					t2.insert(INSERT,lexo1)
					file1=open('redoni2.txt','r')
					lexo=file1.read()
					t5=Text(f,bg='lightblue')
					t5.place(x=683,y=0,height=768,width=683)
					t5.insert(INSERT,lexo)
				else:
					messagebox.showerror("Error", "Passwordi juaj është i gabim")

	labela1=Label(full,text='user',bg='#979599')
	labela1.place(x=10,y=10,width=100,height=20)
	labela2=Label(full,text='Password',bg='#979599')
	labela2.place(x=10,y=50,width=100,height=20)
	dd=Button(full,bg='#979599',text='Log in')
	dd.place(x=120,y=80,width=100,height=30)
	dd.config(command=po)
def stop():
	qwert.destroy()


lo=PhotoImage(file='JC.png')
l=Label(qwert,image=lo,bg="gray")
l.place(x=0,y=0,width=700,height=300)
t3=Text(qwert,bg="gray",bd=2,font=('stika',10),fg="white")
t3.place(x=245,y=335,width=445,height=275)
t3.insert(END,'\t~Udhezimet per perdorim~\n1.Mund te perdoret vetem personat e autorizuar\n2.Askush nga puntoret nuk ka te drejt te prek ne pjeset e pa caktura\n3.hapi i par eshte te keni nje kod per kyqje  te cilin e merrni nga menagjeri\n4.Secili kod dhe puntor ka sektorin e vet te punes\n5.ne pjesen e restorantit gjat shtypjes se faktures ne qoftese ndodh ndonje gabim ateher ka mundesi te fshihet por vetem para shtypjes\n6.Kujdes shtypja e pinit behet vetem ne anen e buttonave ne program\n7.Kyqja nuk behet pa klikuar ne buttonin Kyqu\n8.Kujdes buttoni  eshte i ndaluar te kyqen persona te tjere perpos menagjerit\nPer te kaluar tek faqja e restorantit duhet te shtypni pinin 1234\n1.Pas kyqjes do paraqiteni me programin Restaurant Plaza\n2.Vini re buttoni Log out do ju sjell tek faza fillestare\n3.Keni gjithsej 40 tavolina nga te cialt do zgjedhet duke klikuar ne taolinen perkatese\n4.Ne baze te butonave do selektohet ushqimi, sasia e tij\n5.Fatura do te shfaqet pas zghedhjes se ushqimit\n6.Kujdes butoni mrapa do ju kthej ne hapin paraprak   \nPer te kaluar tek faqja e hotelit duhet te shtypni pinin pinin:4321\nPr tu kyqur te menagjeri duhet te shtpni: Username: Rinor dhe password: 1234 ose Username: Redon dhe password: 4321\n!!Per gjdo problem mbrenda programit ju lutem te kontaktoni shitesin apo krijuesin e programit te cilet mund ti gjeni ne J-Coders Academy ~Gjilan~!!'
)

butooni=Button(qwert,text="Kyqu",font=("Franklin Gothic Demi",10),bg="gray",fg="white",command=loginii)
butooni.place(x=245,y=300,width=100,height=30)

shitjett=Button(qwert,text="Menager",bg="gray",fg="white",font=("Franklin Gothic Demi",10),command=root3)
shitjett.place(x=420,y=300,width=100,height=30)
dalja=Button(qwert,text="Perfundo",font=("Franklin Gothic Demi",10),bg="gray",fg="white",command=stop)
dalja.place(x=589,y=300,width=100,height=30)
frm4=Frame(qwert,bg='gray')
frm4.place(x=0,y=612,width=720,height=22)
lbl = Label(frm4,bg="gray", text='© Copyright by:Rinor Biqku  tel:045-638-783 E-mail:r.biqku342@gmail.com  Gjilan',font=('stika',13),fg='white')
lbl.place(x=50, y=0)




#----------------------------------------------------------------------------------
mainloop()