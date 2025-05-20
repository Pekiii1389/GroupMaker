# GroupMaker

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random

class GroupMakerApp:
    def __init__(self, root):
        # Generating a screen
        self.root = root
        self.root.title("Group Maker")
        self.root.geometry("600x450")

        # Center the window on the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (500 // 2)
        y = (screen_height // 2) - (500 // 2)
        self.root.geometry(f"500x500+{x}+{y}")
        
        # Input for players
        ttk.Label(root, text="Enter Players (comma and space-separated):", font=("Helvetica", 12)).pack(pady=10)
        self.players_entry = ttk.Entry(root, width=50, bootstyle=INFO)
        self.players_entry.pack(pady=10)

        # Example of input
        ttk.Label(root, text="Example: Player1, Player2, Player3...", font=("Helvetica", 10), foreground="gray").pack(pady=2)
        
        # Number of groups
        ttk.Label(root, text="Number of Groups:", font=("Helvetica", 12)).pack(pady=5)
        self.groups_spinbox = ttk.Spinbox(root, from_=2, to=10, width=10, bootstyle=SUCCESS)
        self.groups_spinbox.pack(pady=10)
        
        # Button to generate groups
        ttk.Button(root, text="Generate Groups", command=self.generate_groups, bootstyle=PRIMARY).pack(pady=15)
        
        # Output area
        self.output_frame = ttk.Labelframe(root, text="Generated Groups", bootstyle=INFO, padding=10)
        self.output_frame.pack(fill=ttk.BOTH, expand=True, padx=10, pady=10)
        self.output_text = ttk.Text(self.output_frame, width=70, height=15, state='disabled', font=("Courier New", 11))
        self.output_text.pack(fill=ttk.BOTH, expand=True)
    
    def generate_groups(self):
        """Generate groups from the input players."""
        players = self.players_entry.get().split(", ")
        num_groups = int(self.groups_spinbox.get())
        
        # Catching if the number of groups are higher than number of players
        if len(players) < num_groups:
            ttk.Messagebox.show_error("Error", "Number of groups cannot exceed number of players!")
            return
        
        # Shuffling players
        random.shuffle(players)
        groups = [[] for _ in range(num_groups)]
        
        # Distribute players into groups
        for i, player in enumerate(players):
            groups[i % num_groups].append(player)
        
        # Display groups
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, ttk.END)
        for i, group in enumerate(groups):
            self.output_text.insert(ttk.END, f"Group {i+1}: {', '.join(group)}\n")
        self.output_text.config(state='disabled')


# Run the Group Maker App
if __name__ == "__main__":
    root = ttk.Window(themename="flatly")
    app = GroupMakerApp(root)
    root.mainloop()
