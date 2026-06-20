import argparse

parser = argparse.ArgumentParser(description = "simple calculator")

parser.add_argument("num1", type="float", help = "first number")
parser.add_argument("num2", type="float", help = "second number")
parser.add_argument("operation", choices= ["add","sub", "mul"], help="Operation to perform")


args = parser.parse_args()

print(args)
if(args.operation == "add"):
    print(f"the result is {args.num1 + args.num2}")
elif(args.operation == "add"):
    print(f"the result is {args.num1 - args.num2}")
elif(args.operation == "add"):
    print(f"the result is {args.num1 * args.num2}")
elif(args.operation == "add"):
    print(f"the result is {args.num1 / args.num2}")
else:
    print("some error occurredp")