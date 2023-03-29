from tkinter import messagebox
import customtkinter

from lane import Lane

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

class GUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.lane = Lane()

        # configure window
        self.title("Calculate Lane Info")
        self.geometry(f"{1500}x{580}")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # WAYPOINT ENTRIES
        self.input_frame = customtkinter.CTkFrame(self)
        self.input_frame.rowconfigure((0,1,2,3,4,5,6,7,8,9,10,11,12), weight=1)
        self.input_frame.grid(column=0, row=0, rowspan=2, sticky='ns', padx=10)
        self.input_label = customtkinter.CTkLabel(self.input_frame,text="Waypoint Entry", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.input_label.grid(row=0, column=0, columnspan=2)

        self.waypoint_entries = []
        for i in range(10):
            entry = customtkinter.CTkEntry(self.input_frame, placeholder_text=f'Stop {i+1}')
            entry.grid(row=i+1, column=1, padx=20, pady=10)
            self.waypoint_entries.append(entry)

        self.waypoint_entry_button = customtkinter.CTkButton(self.input_frame, text='Get Lane Details',command= self.get_entry_values)
        self.waypoint_entry_button.grid(row=12, columnspan=4, pady=10)

        #ROUTE INFO
        self.route_frame = customtkinter.CTkFrame(self)
        self.route_frame.columnconfigure(2, weight=1)
        self.route_frame.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
        self.cost_per_mile_label = customtkinter.CTkLabel(self.route_frame,text=f'${self.lane.cost_per_mile} ', font=customtkinter.CTkFont(size=30, weight="bold"))
        self.cost_per_mile_label.grid(row=0, column=0)
        self.cost_per_mile_button = customtkinter.CTkButton(self.route_frame, text=f'Update Cost Per Mile', command=self.open_cost_per_mile_dialog)
        self.cost_per_mile_button.grid(row=0, column=1)
        self.logo_label = customtkinter.CTkLabel(self.route_frame, text="Routes", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=2, sticky='ew')
        self.recalculate_button = customtkinter.CTkButton(self.route_frame, text='Calculate Totals', state='disabled', command=self.update_total_frame)
        self.recalculate_button.grid(column=3, row=0, padx=10, pady=10)

        #TOTALS INFO
        #LABELS
        self.total_frame = customtkinter.CTkFrame(self)
        self.total_frame.columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.total_frame.grid(row=1, column=1, sticky='nsew',padx=10, pady=10)
        self.total_miles_label = customtkinter.CTkLabel(self.total_frame, text="Total Miles", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.total_miles_label.grid(row=0, column=0, sticky='new')
        self.total_empy_miles_label = customtkinter.CTkLabel(self.total_frame, text="Empty Miles", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.total_empy_miles_label.grid(row=0, column=1, sticky='new')
        self.deadhead_percent_label = customtkinter.CTkLabel(self.total_frame, text="Deadhead Percent", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.deadhead_percent_label.grid(row=0, column=2, sticky='new')
        self.total_cost_label = customtkinter.CTkLabel(self.total_frame, text="Total Cost", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.total_cost_label.grid(row=0, column=3, sticky='new')
        self.total_revenue_label = customtkinter.CTkLabel(self.total_frame, text="Total Revenue", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.total_revenue_label.grid(row=0, column=4, sticky='new')
        self.difference_label = customtkinter.CTkLabel(self.total_frame, text="Difference", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.difference_label.grid(row=0, column=5, sticky='new')
        self.rate_per_mile_label = customtkinter.CTkLabel(self.total_frame, text="RPM", font=customtkinter.CTkFont(size=25, weight="bold", underline=True))
        self.rate_per_mile_label.grid(row=0, column=6, sticky='new')

        #ACTUALS
        self.total_miles = customtkinter.CTkLabel(self.total_frame, text='0.0 Miles', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.total_miles.grid(row=1, column=0, sticky='new', pady=10)
        self.total_empty_miles = customtkinter.CTkLabel(self.total_frame, text='0.0 Miles', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.total_empty_miles.grid(row=1, column=1, sticky='new', pady=10)
        self.deadhead_percent = customtkinter.CTkLabel(self.total_frame, text='0.0%', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.deadhead_percent.grid(row=1, column=2, sticky='new', pady=10)
        self.total_cost = customtkinter.CTkLabel(self.total_frame, text=f'$0.00', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.total_cost.grid(row=1, column=3, sticky='new', pady=10)
        self.total_revenue = customtkinter.CTkLabel(self.total_frame, text=f'$0.00', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.total_revenue.grid(row=1, column=4, sticky='new', pady=10)
        self.difference = customtkinter.CTkLabel(self.total_frame, text=f'$0.00', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.difference.grid(row=1, column=5, sticky='new', pady=10)
        self.rate_per_mile = customtkinter.CTkLabel(self.total_frame, text=f'$0.00', font=customtkinter.CTkFont(size=20, weight="bold"))
        self.rate_per_mile.grid(row=1, column=6, sticky='new', pady=10)

    def update_total_frame(self):
        self.calculate_total_revenue()
        self.lane.get_totals()

        self.total_miles.configure(text=f'{round(self.lane.total_distance, 2)} Miles')
        self.total_empty_miles.configure(text=f'{round(self.lane.empty_distance, 2)} Miles')
        self.deadhead_percent.configure(text=f'{round(self.lane.deadhead_percent, 2)}%')
        self.total_cost.configure(text=f'${format(round(self.lane.total_cost, 2), ".2f")}')
        self.total_revenue.configure(text=f'${format(round(self.lane.total_revenue, 2), ".2f")}')
        self.difference.configure(text=f'${format(round(self.lane.cost_difference, 2), ".2f")}')
        self.rate_per_mile.configure(text=f'${format(round(self.lane.rate_per_mile, 2), ".2f")}')

    def open_cost_per_mile_dialog(self):
        dialog = customtkinter.CTkInputDialog(text="Enter new Cost Per Mile:", title="Cost Per Mile")
        print('Cost Per mile was successfully changed')
        self.lane.cost_per_mile =  float(dialog.get_input())
        self.cost_per_mile_label.configure(text=f'${format(self.lane.cost_per_mile, ".3f")} ')

    def get_entry_values(self):
        for entry in self.waypoint_entries:
            value = entry.get().upper()
            if len(value) > 0:
                self.lane.waypoints.append(value)
        self.lane.create_routes()
        self.update_route_frame()

    def update_route_frame(self):
        self.rate_per_mile_entries = []

        if len(self.lane.routes) > 0:
            self.recalculate_button.configure(state='normal')

            for i, route in enumerate(self.lane.routes):
                route_row = customtkinter.CTkFrame(self.route_frame)
                route_row.grid(column=0, columnspan=4, row=i+1, sticky='ew', pady=5, padx=5)
                route_row.columnconfigure(0, weight=1)

                route_label = customtkinter.CTkLabel(route_row, text=f'{route.origin.city}, {route.origin.state} to {route.destination.city}, {route.destination.state} - {round(route.distance)} Miles', height=20, font=customtkinter.CTkFont(size=20, weight="bold"))
                route_label.grid(column=0, columnspan=2, row=0, sticky='w', padx=5)

                checkbox = customtkinter.CTkCheckBox(route_row, text='Loaded?', font=customtkinter.CTkFont(size=15, weight="bold"), command=route.toggle_is_loaded)
                checkbox.select()
                checkbox.grid(column=2, row=0, sticky='ew', padx=5)

                entry_label = customtkinter.CTkLabel(route_row, text='RPM: $', font=customtkinter.CTkFont(size=15, weight='bold'))    
                entry_label.grid(column=3, row=0, sticky='ew', padx=5)
                entry = customtkinter.CTkEntry(route_row)
                entry.insert(0, format(route.rate_per_mile, '.2f'))
                entry.grid(column=4, row=0, sticky='ew', padx=5)
                
                self.rate_per_mile_entries.append(entry)
        else:
            pass

    def calculate_total_revenue(self):
        for i, route in enumerate(self.lane.routes):
            route.update_rate_per_mile(float(self.rate_per_mile_entries[i].get()))
            route.calculate_route_revenue()