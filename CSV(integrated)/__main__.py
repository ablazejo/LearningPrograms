from argparse import ArgumentParser
from data_class import User_Message


parser = ArgumentParser(prog="Programy")
parser.add_argument("type", type=str, choices=["view", "message", "to_all"])
parser.add_argument("--id", type=int)
parser.add_argument("--email", type=str)

args = parser.parse_args()
obj = User_Message()

if args.type == "view":
	print(obj.read_data(user_id=args.id, email=args.email))
if args.type == "message":
	print(obj.send_message(user_id=args.id, email=args.email))
if args.type == "to_all":
	print(obj.send_to_all())

	
