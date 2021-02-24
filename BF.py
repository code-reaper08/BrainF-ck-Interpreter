import sys

f = open(sys.argv[1], "r")
program_to_read = f.read()
f.close()

programPosition = 0

memory = [0]
memoryPosition = 0

while programPosition < len(program_to_read):
	if program_to_read[programPosition] == ">":
		memoryPosition += 1
		if len(memory) <= memoryPosition:
			memory.append(0)
			
	elif program_to_read[programPosition] == "<":
		memoryPosition -= 1
		if memoryPosition < 0:
			print("Error: Moved off tape!")
			sys.exit(0)
		
	elif program_to_read[programPosition] == "+":
		memory[memoryPosition] += 1
		if memory[memoryPosition] > 255:
			memory[memoryPosition] = 0
		
	elif program_to_read[programPosition] == "-":
		memory[memoryPosition] -= 1
		if memory[memoryPosition] <= -1:
			memory[memoryPosition] = 255
		
	elif program_to_read[programPosition] == ".":
		print(chr(memory[memoryPosition]), end="")
		
	elif program_to_read[programPosition] == ",":
		inp = input("Input requested: ")
		memory[memoryPosition] = ord( inp[0] )
		
	elif program_to_read[programPosition] == "[":
		if memory[memoryPosition] == 0:
			OpenBracketCount = 0
			programPosition += 1
			while programPosition < len(program_to_read):
				if program_to_read[programPosition] == "]" and OpenBracketCount == 0:
					break
				elif program_to_read[programPosition] == "[":
					OpenBracketCount += 1
				elif program_to_read[programPosition] == "]":
					OpenBracketCount -= 1
				programPosition += 1
				
	elif program_to_read[programPosition] == "]":
		if memory[memoryPosition] != 0:
			ClosedBracketCount = 0
			programPosition -= 1
			while programPosition >= 0:
				if program_to_read[programPosition] == "[" and ClosedBracketCount == 0:
					break
				elif program_to_read[programPosition] == "]":
					ClosedBracketCount += 1
				elif program_to_read[programPosition] == "[":
					ClosedBracketCount -= 1
				programPosition -= 1

	programPosition += 1
	
print("")
