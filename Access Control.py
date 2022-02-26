import os

def main_help():
	print("0. EXIT")
	print("1. CHANGE PERMISSION")
	print("2. CHANGE OWNER")
	print("3. CHANGE GROUP")

main_help()
while True:
	select = input("access control >> ")
	if select == '0':
		print("BYE\n")
		break

	elif select == '1':
		os.system("ls")
		selected_file = input("access control > Enter File or Directory name: ")
		owner_perm = input(f"access control > [{selected_file}] >  owner: ")
		group_perm = input(f"access control > [{selected_file}] >  group: ")
		others_perm = input(f"access control > [{selected_file}] > others: ")

		if owner_perm != '':
			os.system(f"sudo chmod u-rwx {selected_file}")
			os.system(f"sudo chmod u+{owner_perm} {selected_file}")
			pass
		if group_perm != '':
			os.system(f"sudo chmod g-rwx {selected_file}")
			os.system(f"sudo chmod g+{group_perm} {selected_file}")
			pass
		if others_perm != '':
			os.system(f"sudo chmod o-rwx {selected_file}")
			os.system(f"sudo chmod o+{others_perm} {selected_file}")
			pass
		break

	elif select == '2':
		os.system("ls")
		selected_file = input("access control > Enter File or Directory name: ")
		selected_user = input("access control > Enter user name: ")
		os.system(f"sudo chown {selected_user} {selected_file}")
		break	
	elif select == '3':
		os.system("ls")
		selected_file = input("access control > Enter File or Directory name: ")
		selected_group = input("access control > Enter group name: ")
		break
	elif select == 'help' or select == 'HELP' or select == 'Help' or select == 'h' or select == 'H':
		main_help()
