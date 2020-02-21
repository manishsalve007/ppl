from tkinter import *
import os

def delete1() :
	screen3.destroy()

def delete2() :
	screen4.destroy()

def delete3() :
	screen5.destroy()

def delete4() :
	screen9.destroy()
	screen10.destroy()

def delete5() :
	screen1.destroy()

def delete6() :
	screen11.destroy()

def delete7() :
	screen13.destroy()
	screen14.destroy()

def delete8() :
	screen12.destroy()

def logout() :
	screen8.destroy()

def saved() :
	global screen10
	screen10 = Toplevel(screen)
	screen10.title("Saved")
	screen10.geometry("100x100")
	Label(screen10, text = "Saved").pack()
	Button(screen10, text = "OK", command = delete4).pack()


def save() :
	filename = raw_filename.get()
	notes = raw_notes.get()

	data = open(filename, "w")
	data.write(notes)
	data.close()
	saved()

def create_notes() :
	global raw_filename
	global raw_notes
	global screen9
	raw_filename = StringVar()
	raw_notes = StringVar()

	screen9 = Toplevel(screen)
	screen9.title("Info")
	screen9.geometry("400x300")
	Label(screen9, text = "Please enter your MIS", font = ("Calibri")).pack()
	Entry(screen9, textvariable = raw_filename).pack()
	Label(screen9, text = "").pack()
	Label(screen9, text = "Enter your information below", font = ("Calibri")).pack()
	Entry(screen9, textvariable = raw_notes).pack()
	Label(screen9, text = "").pack()
	Button(screen9, text = "Save", command = save).pack()


def view_notes1() :
	global screen12
	filename = raw_filename1.get()
	data = open(filename, "r")
	data1 = data.read()
	screen12 = Toplevel(screen)
	screen12.title("INFO")
	screen12.geometry("400x400")
	Label(screen12, text = data1, font = ("Calibri", 10)).pack()
	Label(screen12, text = "").pack()
	Button(screen12, text = "Back", width = 10, height = 3, command = delete8).pack()

def view_notes() :
	global raw_filename1
	global screen11
	screen11 = Toplevel(screen)
	screen11.title("DATA")
	screen11.geometry("600x600")
	Label(screen11, text = "Please enter the filename to read the info", font = ("Calibri", 15, "bold")).pack()
	all_files = os.listdir()
	Label(screen11, text = "").pack()
	Label(screen11, text = all_files, font = ("Calibri", 13)).pack()
	raw_filename1 = StringVar()
	Entry(screen11, textvariable = raw_filename1).pack()
	Label(screen11, text = "").pack()
	Button(screen11, text = "OK", width = 10, height = 3, command = view_notes1).pack()
	Label(screen11, text = "").pack()
	Button(screen11, text = "Back", width = 10, height = 3, command = delete6).pack()


def delete_note1() :
	global screen14
	filename3 = raw_filename2.get()
	os.remove(filename3)
	screen14 = Toplevel(screen)
	screen14.title("Delete")
	screen14.geometry("400x400")
	Label(screen14, text = filename3 + " Removed").pack()
	Label(screen14, text = "").pack()
	Button(screen14, text = "back", command = delete7).pack()



def delete_note() :
	global raw_filename2
	global screen13
	screen13 = Toplevel(screen)
	screen13.title("Delete")
	screen13.geometry("400x400")
	Label(screen13, text = "Please enter the filename to delete its info").pack()
	all_files = os.listdir()
	Label(screen13, text = all_files).pack()
	raw_filename2 = StringVar()
	Entry(screen13, textvariable = raw_filename2).pack()
	Button(screen13, text = "OK", command = delete_note1).pack()



def session():
	global screen8
	screen8 = Toplevel(screen)
	screen8.title("Dashboard")
	screen8.geometry("400x400")
	Label(screen8, text = "Welcome to the Dashboard", font = ("Calibri", 15)).pack()
	Label(screen8, text = "").pack()
	Button(screen8, text = "Enter Data", command = create_notes, font = ("Calibri", 13)).pack()
	Button(screen8, text = "View Data", command = view_notes, font = ("Calibri", 13)).pack()
	Button(screen8, text = "Delete Data", command = delete_note, font = ("Calibri", 13)).pack()
	Label(screen8, text = "").pack()
	Button(screen8, text = "LOGOUT", command = logout).pack()



def login_success() :
	'''global screen3
	screen3 = Toplevel(screen)
	screen3.title("Success")
	screen3.geometry("200x150")
	Label(screen3, text = "Login Success", font = (10)).pack()
	Label(screen3, text = "").pack()
	Button(screen3, text = "Ok",width = 8, height = 2, command = delete1).pack()
	'''
	session()

def password_not_recognised() :
	global screen4
	screen4 = Toplevel(screen)
	screen4.title("Failure")
	screen4.geometry("200x150")
	Label(screen4, text = "Incorrect Password", font = (10)).pack()
	Label(screen4, text = "").pack()
	Button(screen4, text = "Ok",width = 8, height = 2, command = delete2).pack()

def user_not_found():
	global screen5
	screen5 = Toplevel(screen)
	screen5.title("Failure")
	screen5.geometry("200x150")
	Label(screen5, text = "User not found!", font = (10)).pack()
	Label(screen5, text = "").pack()
	Button(screen5, text = "Ok",width = 8, height = 2, command = delete3).pack()





def register_user() :
	username_info = username.get()
	password_info = password.get()

	file = open(username_info, "w")
	file.write(username_info + "\n")
	file.write(password_info + "\n")
	file.close()

	username_entry.delete(0, END)
	password_entry.delete(0, END)

	Label(screen1, text = "Registration Successful!!!", fg = "green", font = ("Calibri", 13, "bold")).pack()
	Label(screen1, text = "").pack()
	Button(screen1, text = "Back", command = delete5).pack()


def login_varify() :
	username1 = username_varify.get()
	password1 = password_varify.get()
	username_entry1.delete(0, END)
	password_entry1.delete(0, END)

	screen2.destroy()

	list_of_files = os.listdir()
	if username1 in list_of_files :
		file1 = open(username1, "r")
		varify = file1.read().splitlines()
		if password1 in varify :
			login_success()
			#print("Login Success")
			#Label(screen2, text = "Login Success", fg = "green", font = ("Calibri", 13)).pack()

		else:
			password_not_recognised()
			#print("Incorrect password")
			#Label(screen2, text = "Incorrect password", fg = "green", font = ("Calibri", 13)).pack()

	else :
		user_not_found()
		#Label(screen2, text = "User not found!", fg = "green", font = ("Calibri", 13)).pack()



def register() :
	global screen1
	global username
	global password
	global username_entry
	global password_entry

	screen1 = Toplevel(screen)
	screen1.title("Register")
	screen1.geometry("400x300")

	username = StringVar()
	password = StringVar()

	Label(screen1, text = "Create your Username and Password", font = ("Calibri, 15")).pack()
	Label(screen1, text = "").pack()
	Label(screen1, text = "Username *", font = ("Calibri, 15")).pack()
	username_entry = Entry(screen1, textvariable = username)
	username_entry.pack()
	Label(screen1, text = "Password *", font = ("Calibri, 15")).pack()
	password_entry = Entry(screen1, textvariable = password)
	password_entry.pack()
	Label(screen1, text = "").pack()
	Button(screen1, text = "Register", width = "10", height = "2", command = register_user).pack()



def login() :
	global screen2
	global username_entry1
	global password_entry1
	global username_varify
	global password_varify
	screen2 = Toplevel(screen)
	screen2.title("MIS Login")
	screen2.geometry("300x250")
	Label(screen2, text = "Enter the details below to Login", font = ("Calibri", 11, "bold")).pack()
	Label(screen2, text = "").pack()

	username_varify = StringVar()
	password_varify = StringVar()

	Label(screen2, text = "Username *", font = ("Calibri, 15")).pack()
	username_entry1 = Entry(screen2, textvariable = username_varify)
	username_entry1.pack()
	Label(screen2, text = "").pack()
	Label(screen2, text = "Password *", font = ("Calibri, 15")).pack()
	password_entry1 = Entry(screen2, textvariable = password_varify)
	password_entry1.pack()
	Label(screen2, text = "").pack()
	Button(screen2, text = "Login", width = "10", height = "2", command = login_varify).pack()



def main_screen():
	global screen
	screen = Tk()
	screen.geometry("600x400")
	screen.title("MIS Panel")
	Label(text = "Welcome to The MIS Panel", bg = "Yellow", height = "5", width = "190", font = ("Calibri", 15, "bold")).pack()
	Label(text = "").pack()
	Button(text = "Login", height = "4", width = "60", command = login, font = ("Times", 10)).pack()
	Label(text = "").pack()
	Button(text = "Register", height = "4", width = "60", command = register, font = ("Calibri", 10)).pack()

	screen.mainloop()

main_screen()