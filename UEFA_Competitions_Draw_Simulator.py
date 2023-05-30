import tkinter as tk
import random

class DrawSimulator(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("UEFA League Draw Simulator")
        self.pack()
        
        self.league_choices = ["UEFA Champions League", "UEFA Europa League", "UEFA Conference League"]
        self.stage_choices = {
            "UEFA Champions League": ["Group Stage", "Round of 16", "Quarter Finals"],
            "UEFA Europa League": ["Group Stage", "Playoffs", "Round of 16", "Quarter Finals"],
            "UEFA Conference League": ["Group Stage", "Playoffs", "Round of 16", "Quarter Finals"]
        }
        
        self.create_widgets()
        
    def create_widgets(self):
        self.league_label = tk.Label(self, text="Choose a League:")
        self.league_label.pack()
        
        self.league_var = tk.StringVar(self)
        self.league_var.set(self.league_choices[0])
        self.league_menu = tk.OptionMenu(self, self.league_var, *self.league_choices, command=self.update_stage_menu)
        self.league_menu.pack()
        
        self.stage_label = tk.Label(self, text="Choose a Stage:")
        self.stage_label.pack()
        
        self.stage_var = tk.StringVar(self)
        self.stage_var.set(self.stage_choices[self.league_var.get()][0])
        self.stage_menu = tk.OptionMenu(self, self.stage_var, *self.stage_choices[self.league_var.get()])
        self.stage_menu.pack()
        
        self.teams_label = tk.Label(self, text="Enter Teams (Team Name, Country):")
        self.teams_label.pack()
        
        self.teams_text = tk.Text(self, height=10, width=50)
        self.teams_text.pack()
        
        self.draw_button = tk.Button(self, text="Simulate Draw", command=self.simulate_draw)
        self.draw_button.pack()
        
        self.result_label = tk.Label(self, text="")
        self.result_label.pack()
        
    def update_stage_menu(self, league):
        menu = self.stage_menu["menu"]
        menu.delete(0, "end")
        for stage in self.stage_choices[league]:
            menu.add_command(label=stage, command=lambda value=stage: self.stage_var.set(value))
        self.stage_var.set(self.stage_choices[league][0])
        
    def simulate_draw(self):
        league = self.league_var.get()
        stage = self.stage_var.get()
        teams = self.teams_text.get("1.0", tk.END).strip().split("\n")
        
        if league == "UEFA Champions League":
            if stage == "Group Stage":
                self.simulate_champions_group_stage(teams)
            elif stage == "Round of 16":
                self.simulate_round_of_16(teams)
            elif stage == "Quarter Finals":
                self.simulate_quarter_finals(teams)
        elif league == "UEFA Europa League":
            if stage == "Group Stage":
                self.simulate_europa_group_stage(teams)
            elif stage == "Playoffs":
                self.simulate_playoffs(teams)
            elif stage == "Round of 16":
                self.simulate_round_of_16(teams)
            elif stage == "Quarter Finals":
                self.simulate_quarter_finals(teams)
        elif league == "UEFA Conference League":
            if stage == "Group Stage":
                self.simulate_conference_group_stage(teams)
            elif stage == "Playoffs":
                self.simulate_playoffs(teams)
            elif stage == "Round of 16":
                self.simulate_round_of_16(teams)
            elif stage == "Quarter Finals":
                self.simulate_quarter_finals(teams)
                
    def simulate_champions_group_stage(self, teams):
        if len(teams) != 32:
            self.result_label.config(text="Error: 32 teams are required for the Champions League group stage.")
            return
        
        groups = {chr(65 + i): [] for i in range(4)}
        pots = [teams[:8], teams[8:16], teams[16:24], teams[24:]]
        
        for pot in pots:
            random.shuffle(pot)
        
        for i in range(8):
            for j in range(4):
                team = pots[j].pop(0)
                groups[chr(65 + j)].append(team)
        
        if self.check_duplicate_nations(groups):
            self.simulate_champions_group_stage(teams)
        else:
            self.display_results(groups)
        
    def simulate_europa_group_stage(self, teams):
        if len(teams) != 32:
            self.result_label.config(text="Error: 32 teams are required for the Europa League group stage.")
            return
        
        groups = {chr(65 + i): [] for i in range(4)}
        pots = [teams[:8], teams[8:16], teams[16:24], teams[24:]]
        
        for pot in pots:
            random.shuffle(pot)
        
        for i in range(8):
            for j in range(4):
                team = pots[j].pop(0)
                groups[chr(65 + j)].append(team)
        
        if self.check_duplicate_nations(groups):
            self.simulate_europa_group_stage(teams)
        else:
            self.display_results(groups)
        
    def simulate_conference_group_stage(self, teams):
        if len(teams) != 32:
            self.result_label.config(text="Error: 32 teams are required for the Conference League group stage.")
            return
        
        groups = {chr(65 + i): [] for i in range(4)}
        pots = [teams[:8], teams[8:16], teams[16:24], teams[24:]]
        
        for pot in pots:
            random.shuffle(pot)
        
        for i in range(8):
            for j in range(4):
                team = pots[j].pop(0)
                groups[chr(65 + j)].append(team)
        
        if self.check_duplicate_nations(groups):
            self.simulate_conference_group_stage(teams)
        else:
            self.display_results(groups)
        
    def simulate_playoffs(self, teams):
        if len(teams) != 16:
            self.result_label.config(text="Error: 16 teams are required for the playoffs.")
            return
        
        random.shuffle(teams)
        match_pairs = [(teams[i], teams[i + 8]) for i in range(8)]
        
        if self.check_duplicate_nations(match_pairs):
            self.simulate_playoffs(teams)
        else:
            self.display_results(match_pairs)
        
    def simulate_round_of_16(self, teams):
        if len(teams) != 16:
            self.result_label.config(text="Error: 16 teams are required for the round of 16.")
            return
        
        random.shuffle(teams)
        match_pairs = [(teams[i], teams[i + 8]) for i in range(8)]
        
        if self.check_duplicate_nations(match_pairs):
            self.simulate_round_of_16(teams)
        else:
            self.display_results(match_pairs)
        
    def simulate_quarter_finals(self, teams):
        if len(teams) != 8:
            self.result_label.config(text="Error: 8 teams are required for the quarter finals.")
            return
        
        random.shuffle(teams)
        match_pairs = [(teams[i], teams[i + 1]) for i in range(0, 8, 2)]
        
        self.display_results(match_pairs)
        
    def check_duplicate_nations(self, groups_or_match_pairs):
        for key in groups_or_match_pairs:
            nations = [team.split(", ")[1] for team in groups_or_match_pairs[key]]
            if len(set(nations)) != 8:
                return True
        return False
        
    def display_results(self, groups_or_match_pairs):
        if isinstance(groups_or_match_pairs, dict):
            results = ""
            for group, teams in groups_or_match_pairs.items():
                results += f"Group {group}:\n"
                for team in teams:
                    results += f"{team.split(', ')[0]} ({team.split(', ')[1]})\n"
                results += "\n"
        else:
            results = ""
            for i, match in enumerate(groups_or_match_pairs):
                results += f"Match {i + 1}: {match[0].split(', ')[0]} ({match[0].split(', ')[1]}) vs. {match[1].split(', ')[0]} ({match[1].split(', ')[1]})\n"
        
        self.result_label.config(text=results)
        
root = tk.Tk()
app = DrawSimulator(master=root)
app.mainloop()
