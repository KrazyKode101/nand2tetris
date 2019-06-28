// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(LOOP)

	@KBD
	D=M

	@KEYPRESSED
	D;JNE

	(KEYNOTPRESSED)
	@val
	M=0
	@SETPIXELS
	0;JMP

	(KEYPRESSED)
	@val
	M=-1

	(SETPIXELS)

		@SCREEN
		D=A
		@addr
		M=D

		@256
		D=A
		@numrows
		M=D

		(FORALLROWS)

			@numrows
			M=M-1
			D=M

			@END
			D;JLT

			@32
			D=A
			@numcols
			M=D

			(FORALLCOLS)

				@numcols
				M=M-1
				D=M

				@FORALLROWS
				D;JLT
				
				@val
				D=M
				@addr
				A=M
				M=D

				@addr
				M=M+1

				@FORALLCOLS
				0;JMP

	(END)
		@LOOP
		0;JMP