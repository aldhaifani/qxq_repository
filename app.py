import base64
import cirq
from random import choices
from tkinter import *


class QKDDemo:
    def __init__(self, master):
        self.master = master
        master.title("Quantum Key Distribution Demonstration")
        root.geometry("900x800")  # Set window size to 900x800

        # quantum variables
        self.encode_gates = {0: cirq.I, 1: cirq.X}
        self.basis_gates = {"Z": cirq.I, "X": cirq.H}

        self.qubits = None

        self.alice_key = []
        self.final_alice_key = []
        self.alice_bases = []
        self.alice_circuit = None

        self.bob_key = []
        self.final_bob_key = []
        self.bob_bases = []
        self.bob_circuit = None

        self.message = StringVar()
        self.num_bits = IntVar()
        self.current_step = 1  # Start step counter from 1

        self.encrypted_msg = ""

        # Create UI elements
        self.message_label = Label(master, text="Enter Message:")
        self.message_entry = Entry(master, textvariable=self.message)
        self.bits_label = Label(master, text="Number of Bits for Key:")
        self.bits_entry = Entry(master, textvariable=self.num_bits)
        self.start_button = Button(master, text="Start", command=self.start_simulation)

        # Left column frame for step counter and next button
        self.left_column_frame = Frame(master)
        self.step_label = Label(
            self.left_column_frame, text="Step {}:".format(self.current_step)
        )  # Update initial step text
        self.next_button = Button(
            self.left_column_frame,
            text="Next Step",
            state=DISABLED,
            command=self.next_step,
        )

        self.step_text_frame = Frame(
            master
        )  # Create a frame for step text in right column
        self.step_text = Label(
            self.step_text_frame,
            text="",
            width=80,
            bg="white",
            anchor="w",  # Set anchor to 'w' for left alignment
            fg="black",
            justify=LEFT,
        )  # Set fixed width, enable wrapping, white background, and left alignment

        self.step_text_frame.config(
            bg="white", padx=10, pady=10, height=400
        )  # Set white background, padding

        self.restart_button = Button(
            master, text="Restart", state=DISABLED, command=self.restart
        )  # Corrected typo here
        self.thank_you_label = Label(master, text="")

        # Layout UI elements
        self.message_label.grid(row=0, column=0)
        self.message_entry.grid(row=0, column=1)
        self.bits_label.grid(row=1, column=0)
        self.bits_entry.grid(row=1, column=1)
        self.start_button.grid(row=2, columnspan=2, pady=10)  # Add padding below

        # Left column
        self.left_column_frame.grid(row=3, column=0)
        self.step_label.pack()  # Pack step label and next button within the left column frame
        self.next_button.pack()

        # Right column - Grid with fixed row height for explanation text
        self.step_text_frame.grid(row=3, column=1, sticky="nsew", padx=10, pady=10)
        self.step_text.grid(
            row=0, column=0
        )  # Step text within the right column frame (row 0)

        # Set fixed height for the row where the explanation text resides (row 3)
        master.grid_rowconfigure(3, minsize=600)

        self.restart_button.grid(row=4, columnspan=2)
        self.thank_you_label.grid(row=5, columnspan=2)

    def start_simulation(self):
        # Get user input and validate
        message = self.message.get()
        num_bits = self.num_bits.get()
        if not message or not num_bits:
            self.step_text.config(text="Please enter a message and number of bits.")
            return

        # Reset simulation variables (excluding step counter)
        self.qubits = cirq.NamedQubit.range(num_bits, prefix="q")

        self.alice_key = []
        self.alice_bases = []
        self.alice_circuit = None

        self.bob_key = []
        self.bob_bases = []
        self.bob_circuit = None

        # Enable next step button
        self.next_button.config(state=NORMAL)
        self.start_button.config(state=DISABLED)
        self.message_entry.config(state=DISABLED)
        self.bits_entry.config(state=DISABLED)

        # Update the step label to display "Step 1:" initially
        self.step_label.config(text="Step {}:".format(self.current_step))

        self.show_step()

    def next_step(self):
        if self.current_step == 1:
            # Step 3: Alice generates keys
            self.show_step()
        elif self.current_step == 2:
            # Step 4: Alice picks random bases
            self.show_step()
        elif self.current_step == 3:
            # Step 5: Alice creates qubits
            self.show_step()
        elif self.current_step == 4:
            # Step 6: Alice sends qubits to Bob (simulated)
            self.show_step()
        elif self.current_step == 5:
            # Step 7: Bob picks random bases
            self.show_step()
        elif self.current_step == 6:
            # Step 8: Bob applies bases to qubits (simulated)
            self.show_step()
        elif self.current_step == 7:
            # Step 9: Bob measures qubits (simulated)
            self.show_step()
        elif self.current_step == 8:
            # Step 10: Alice and Bob share random bases
            self.show_step()
        elif self.current_step == 9:
            # Step 11: Compare bases and discard mismatched qubits
            self.show_step()
        elif self.current_step == 10:
            # Step 12: Alice and Bob compare key slices
            self.show_step()
        elif self.current_step == 11:
            # Step 13: Alice encrypts message
            self.show_step()
        elif self.current_step == 12:
            # Step 14: Bob decrypts message
            self.show_step()
            self.thank_you_label.config(
                text="Thank you for using the QKD simulator! You can restart the simulation if you wish."
            )
            self.restart_button.config(state=NORMAL)
            self.next_button.config(state=DISABLED)
        self.current_step += 1
        self.step_label.config(text="Step {}:".format(self.current_step))

    def show_step(self):
        step_text = ""
        if self.current_step == 1:
            step_text = self.step_1()
        elif self.current_step == 2:
            step_text = self.step_2()
        elif self.current_step == 3:
            step_text = self.step_3()
        elif self.current_step == 4:
            step_text = self.step_4()
        elif self.current_step == 5:
            step_text = self.step_5()
        elif self.current_step == 6:
            step_text = self.step_6()
        elif self.current_step == 7:
            step_text = self.step_7()
        elif self.current_step == 8:
            step_text = self.step_8()
        elif self.current_step == 9:
            step_text = self.step_9()
        elif self.current_step == 10:
            step_text = self.step_10()
        elif self.current_step == 11:
            step_text = self.step_11()
        elif self.current_step == 12:
            step_text = self.step_12()
        # ... (similar logic for other steps)
        self.step_text.config(text=step_text)

    def restart(self):
        # Reset simulation and UI elements for restart
        self.message.set("")
        self.num_bits.set(0)

        self.qubits = None

        self.alice_key = []
        self.alice_bases = []
        self.alice_circuit = None

        self.bob_key = []
        self.bob_bases = []
        self.bob_circuit = None

        self.next_button.config(state=DISABLED)
        self.start_button.config(state=NORMAL)
        self.message_entry.config(state=NORMAL)
        self.bits_entry.config(state=NORMAL)
        self.step_text.config(text="")
        self.thank_you_label.config(text="")

    def step_1(self):
        """Returns the text for the step #1"""
        num_bits = self.num_bits.get()

        self.alice_key = choices([0, 1], k=num_bits)
        text = "Alice generates a random secret key of {} bits. \nAlice's random key: {}".format(
            num_bits, self.alice_key
        )
        return text

    def step_2(self):
        """Returns the text for step #2"""

        self.alice_bases = choices(["Z", "X"], k=self.num_bits.get())

        text = "Alice randomly chooses between the Z basis (|+> or |->) and the X basis (|0> or |1>) for each qubit in the key. \nAlice's random bases: {}".format(
            self.alice_bases
        )
        return text

    def step_3(self):
        """Returns the text for step #3"""

        self.alice_circuit = cirq.Circuit()

        for i in range(self.num_bits.get()):

            encode_value = self.alice_key[i]
            encode_gate = self.encode_gates[encode_value]

            basis_value = self.alice_bases[i]
            basis_gate = self.basis_gates[basis_value]

            qubit = self.qubits[i]
            self.alice_circuit.append(encode_gate(qubit))
            self.alice_circuit.append(basis_gate(qubit))

        text = "Alice prepares the qubits in the chosen bases and sends them to Bob over a quantum channel.\n\nAlice's Circuit:\n{}".format(
            str(self.alice_circuit)
        )
        return text

    def step_4(self):
        """Returns the text for step #4"""

        text = "Alice sends the qubits to Bob"
        return text

    def step_5(self):
        """Returns the text for step #5"""

        self.bob_bases = choices(["Z", "X"], k=self.num_bits.get())

        text = "Bob randomly chooses between the Z basis (|+> or |->) and the X basis (|0> or |1>) for each qubit in the key. \nBob's random bases: {}".format(
            self.bob_bases
        )
        return text

    def step_6(self):
        """Returns the text for step #6"""

        self.bob_circuit = cirq.Circuit()

        for i in range(self.num_bits.get()):

            basis_value = self.bob_bases[i]
            basis_gate = self.basis_gates[basis_value]

            qubit = self.qubits[i]
            self.bob_circuit.append(basis_gate(qubit))

        text = "Bob applies to the qubits the chosen bases.\nBob's Circuit:\n{}".format(
            str(self.bob_circuit)
        )
        return text

    def step_7(self):
        """Returns the text for step #7"""

        self.bob_circuit.append(cirq.measure(self.qubits, key="bob key"))

        bb84_circuit = self.alice_circuit + self.bob_circuit

        sim = cirq.Simulator()
        results = sim.run(bb84_circuit)
        self.bob_key = results.measurements["bob key"][0]

        text = "Bob measures the qubits and gets the following key:\n{}".format(
            self.bob_key
        )
        return text

    def step_8(self):
        """Returns the text for step #8"""

        text = "Alice and Bob share the random bases they used and compare them.\nAlice's Bases: {}\nBob's Bases:  {}".format(
            self.alice_bases, self.bob_bases
        )
        return text

    def step_9(self):
        """Returns the text for step #9"""
        for bit in range(self.num_bits.get()):

            if self.alice_bases[bit] == self.bob_bases[bit]:
                self.final_alice_key.append(self.alice_key[bit])
                self.final_bob_key.append(self.alice_key[bit])
            else:
                continue

        text = "For every qubit, if the bases match they keep the qubit else they discard that specific qubit.\nFinal Alice's key: {}\nFinal Bob's key:  {}".format(
            self.final_alice_key, self.final_bob_key
        )
        return text

    def step_10(self):
        """Returns the text for step #10"""

        text = "Alice and Bob share the last 3 digits of the key and compare them;\nif they differ, that means there has been an interception so they need to restart or change the communication channel.\nOtherwise, if it matches, that means they can continue\n"
        text += "Alice's last 3 digits of the key: {}\n".format(
            self.final_alice_key[-3:]
        )
        text += "Bob's last 3 digits of the key:   {}\n".format(self.final_bob_key[-3:])
        text += "The keys match, so we can continue!"
        return text

    def step_11(self):
        """Returns the text for step #11"""
        msg = self.message.get()
        key_str = ""
        for c in self.final_alice_key:
            key_str += str(c)
        self.encrypted_msg = self.encrypt(key_str, msg)

        text = "Alice encrypts the message according to the generated key and sends it to Bob.\n"
        text += "Using a simple encryption method, we get the following: \n {}".format(
            self.encrypted_msg
        )
        return text

    def step_12(self):
        """Returns the text for step #12"""

        key_str = ""
        for c in self.final_bob_key:
            key_str += str(c)

        text = "Bob decrypts the encrypted message according to the generated key and get the message.\n"
        text += "Using a simple decryption method, we get the following messags: \n {}".format(
            self.decrypt(key_str, self.encrypted_msg)
        )
        return text

    def encrypt(self, key, string):
        """Returns the encrypted version of the given message according to a given key"""
        enc = []
        for i in range(len(string)):
            key_c = key[i % len(key)]
            enc_c = chr((ord(string[i]) + ord(key_c)) % 256)
            enc.append(enc_c)
        return base64.urlsafe_b64encode("".join(enc).encode()).decode()

    def decrypt(self, key, enc):
        """Returns the decrypted version of the given message according to a given key"""
        dec = []
        enc = base64.urlsafe_b64decode(enc).decode()
        for i in range(len(enc)):
            key_c = key[i % len(key)]
            dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
            dec.append(dec_c)
        return "".join(dec)


# Run the main loop to start the GUI application
root = Tk()
qkd_demo = QKDDemo(root)
root.mainloop()
