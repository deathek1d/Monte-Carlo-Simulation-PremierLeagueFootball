import sys
import time
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from prettytable import PrettyTable

print("-------------- Monte Carlo Match Simulator--------------")

num_simulations = 20000
choose = input(csv)

if choose == "csv":
    teams = ()
    points = dict()
    formatted_season = ""
    teams_2122=('Manchester City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal',
                'Manchester Utd', 'West Ham', 'Leicester City', 'Brighton', 'Wolves',
                'Newcastle Utd', 'Crystal Palace', 'Brentford', 'Aston Villa', 'Southampton',
                'Everton', 'Leeds United', 'Burnley', 'Watford', 'Norwich City')
    pts_2122=dict({'Manchester City': 93, 'Liverpool': 92, 'Chelsea': 74, 'Tottenham': 71, 'Arsenal':69,
                   'Manchester Utd': 58, 'West Ham': 56, 'Leicester City': 52, 'Brighton': 51, 'Wolves': 51,
                   'Newcastle Utd': 49, 'Crystal Palace': 48, 'Brentford': 46, 'Aston Villa': 45, 'Southampton': 40,
                   'Everton': 39, 'Leeds United': 38, 'Burnley': 35, 'Watford': 23, 'Norwich City': 22})
    teams_2223=('Manchester City', 'Arsenal', 'Manchester Utd', 'Newcastle Utd', 'Liverpool',
                'Brighton', 'Aston Villa', 'Tottenham', 'Brentford', 'Fulham', 
                'Crystal Palace', 'Chelsea', 'Wolves', 'West Ham', 'Bournemouth',
                'Nottingham Forest', 'Everton', 'Leicester City', 'Leeds United', 'Southampton')
    pts_2223=dict({'Manchester City': 89, 'Arsenal': 84, 'Manchester Utd': 75, 'Newcastle Utd': 71, 'Liverpool': 67,
                   'Brighton': 62, 'Aston Villa': 61, 'Tottenham': 60, 'Brentford': 59, 'Fulham': 52,
                   'Crystal Palace': 45, 'Chelsea': 44, 'Wolves': 41, 'West Ham': 40, 'Bournemouth': 39,
                   'Nottingham Forest': 38, 'Everton': 36, 'Leicester City': 34, 'Leeds United': 31, 'Southampton':25})
    teams_2324=('Manchester City', 'Tottenham', 'Liverpool', 'West Ham', 'Arsenal', 
                'Brighton', 'Crystal Palace', 'Brentford', 'Nottingham Forest', 'Aston Villa', 
                'Manchester Utd', 'Chelsea', 'Fulham', 'Newcastle Utd', 'Wolves',
                'Bournemouth', 'Sheffield Utd', 'Everton', 'Luton Town', 'Burnley')
    pts_2324=dict({'Liverpool': 82, 'Manchester City': 91, 'Arsenal': 89, 'Aston Villa': 68, 'Tottenham': 66, 
                   'West Ham' : 52, 'Manchester Utd' : 60, 'Brighton':48, 'Chelsea': 63, 'Newcastle Utd': 60,
                   'Wolves': 46, 'Bournemouth': 48, 'Fulham': 47, 'Brentford': 39, 'Crystal Palace': 49,
                   'Nottingham Forest': 32, 'Everton': 40, 'Luton Town': 26, 'Burnley': 24, 'Sheffield Utd': 16})
    teams_2425=('Manchester City', 'Tottenham', 'Liverpool', 'West Ham', 'Arsenal', 
                'Brighton', 'Crystal Palace', 'Brentford', 'Nottingham Forest', 'Aston Villa', 
                'Manchester Utd', 'Chelsea', 'Fulham', 'Newcastle Utd', 'Wolves',
                'Bournemouth', 'Everton', 'Leicester', 'Ipswich', 'Southhampton') 
    pts_2425=dict({'Liverpool': 84, 'Manchester City': 71, 'Arsenal': 74, 'Aston Villa': 66, 'Tottenham': 38, 
                   'West Ham' : 43, 'Manchester Utd' : 42, 'Brighton':61, 'Chelsea': 69, 'Newcastle Utd': 66,
                   'Wolves': 42, 'Bournemouth': 56, 'Fulham': 54, 'Brentford': 56, 'Crystal Palace': 53,
                   'Nottingham Forest': 65, 'Everton': 48, 'Leicester': 25, 'Ipswich': 22, 'Southhampton': 12})               
                
    season = input("* Select season (21/22, 22/23, 23/24, 24/25): ")
    if season == "21/22":
        teams = teams_2122
        points = pts_2122
        formatted_season="2122"
    elif season == "22/23":
        teams = teams_2223
        points = pts_2223
        formatted_season="2223"
    elif season == "23/24":
        teams = teams_2324
        points = pts_2324
        formatted_season="2324"
    elif season == "24/25":
        teams = teams_2425
        points = pts_2425
        formatted_season = "2425"
    else:
        print("Invalid season.")
        sys.exit()
    
    print ("* Will read data from csv file.")
    csv_name = input("* Add csv filename: ")
    filter_team = input("* Filter by team? (Leave blank for all teams, or enter team name): ")
     
    print("----------------------")    
    
    ovl_xpts = 0
    ovl_xgf  = 0
    ovl_xga  = 0
    ovl_xgd  = 0
    
    ovl_xpts_dict = {}
    ovl_xgf_dict = {}
    ovl_xga_dict = {}
    ovl_xgd_dict = {}
    
    for i in teams:
        ovl_xpts_dict[i] = ovl_xpts
        ovl_xgf_dict[i]  = ovl_xgf
        ovl_xga_dict[i]  = ovl_xga
        ovl_xgd_dict[i]  = ovl_xgd
   
    df = pd.read_csv(csv_name)
    filtered_matches = 0
    for i in range(0, len(df)):
        print("* Game #", i+1, "*")
        
        input_home_team = df.iloc[i]['Home_Team']
        input_home_team_xg = df.iloc[i]['xG-H']
        input_away_team = df.iloc[i]['Away_Team']
        input_away_team_xg = df.iloc[i]['xG-A']

        if filter_team and filter_team not in [input_home_team, input_away_team]:
            continue
        
        filtered_matches += 1
        
        if filter_team:
            print(f"* Showing match {filtered_matches} (filtered for {filter_team}) *")
        else:
            print("* Game #", i+1, "*")

        print("* Home team:", input_home_team)
        print("* Away team:", input_away_team)
        print("* Home team xG:", input_home_team_xg)
        print("* Away team xG:", input_away_team_xg)

        print ("* SIMULATION TABLE *")
        print ("*--------------*")
  
        count_home_wins = 0
        count_home_loss = 0
        count_away_wins = 0
        count_away_loss = 0
        count_draws = 0
        score_mat = []
        tot_sim_time = 0
        

        sim_table = PrettyTable(["SIMULATION #", "SIMULATION TIME (s)", input_home_team, input_away_team, "HOME WIN", "AWAY WIN", "DRAW", "SCORE MARGIN"])
       
        for i in range(num_simulations):
            #get simulation start time
            start_time = time.time()
            #run the sim - generate a random Poisson distribution
            target_home_goals_scored = np.random.poisson(input_home_team_xg)
            target_away_goals_scored = np.random.poisson(input_away_team_xg)
            home_win = 0
            away_win = 0
            draw = 0
            margin = 0
            # if more goals for home team => home team wins
            if target_home_goals_scored > target_away_goals_scored:
                count_home_wins += 1
                count_away_loss += 1
                home_win = 1
                margin = target_home_goals_scored - target_away_goals_scored
            # if more goals for away team => away team wins
            elif target_home_goals_scored < target_away_goals_scored:
                count_away_wins += 1
                count_home_loss += 1
                away_win = 1
                margin = target_away_goals_scored - target_home_goals_scored
            elif target_home_goals_scored == target_away_goals_scored:
                draw = 1
                count_draws += 1
                margin = target_away_goals_scored - target_home_goals_scored
            # add score to score matrix
            score_mat.append((target_home_goals_scored, target_away_goals_scored))
            #get end time
            end_time = time.time()
            #add the time to the total simulation time
            tot_sim_time += round((end_time - start_time),5)
            #add the info to the simulation table
            sim_table.add_row([i+1, round((end_time - start_time),5), target_home_goals_scored, target_away_goals_scored, home_win, away_win, draw, margin])
        print(sim_table)

    
        home_win_probability = round((count_home_wins/num_simulations * 100),2)
        away_win_probability = round((count_away_wins/num_simulations * 100),2)
        draw_probability = round((count_draws/num_simulations * 100),2)

        print ("* SIM STATS *")
        sim_table_stats = PrettyTable(["Total # of sims", "Total time (s) for sims", "HOME WINS", "AWAY WINS", "DRAWS"])
        sim_table_stats.add_row([num_simulations, round(tot_sim_time,3), count_home_wins, count_away_wins, count_draws])
        sim_table_stats.add_row(["-", "-", str(home_win_probability)+"%", str(away_win_probability)+"%", str(draw_probability)+"%"])
        print(sim_table_stats)
        
   
        total_scores = len(score_mat)
        max_score = 5
        assemble_scores = [[0 for x in range(max_score)] for y in range(max_score)]
        for i in range(total_scores):
            if score_mat[i][0] == 0 and score_mat[i][1] == 0:
                assemble_scores[0][0] += 1
            elif score_mat[i][0] == 0 and score_mat[i][1] == 1:
                assemble_scores[0][1] += 1
            elif score_mat[i][0] == 0 and score_mat[i][1] == 2:
                assemble_scores[0][2] += 1
            elif score_mat[i][0] == 0 and score_mat[i][1] == 3:
                assemble_scores[0][3] += 1  
            elif score_mat[i][0] == 0 and score_mat[i][1] == 4:
                assemble_scores[0][4] += 1    
            elif score_mat[i][0] == 1 and score_mat[i][1] == 0:
                assemble_scores[1][0] += 1
            elif score_mat[i][0] == 1 and score_mat[i][1] == 1:
                assemble_scores[1][1] += 1     
            elif score_mat[i][0] == 1 and score_mat[i][1] == 2:
                assemble_scores[1][2] += 1     
            elif score_mat[i][0] == 1 and score_mat[i][1] == 3:
                assemble_scores[1][3] += 1     
            elif score_mat[i][0] == 1 and score_mat[i][1] == 4:
                assemble_scores[1][4] += 1
            elif score_mat[i][0] == 2 and score_mat[i][1] == 0:
                assemble_scores[2][0] += 1
            elif score_mat[i][0] == 2 and score_mat[i][1] == 1:
                assemble_scores[2][1] += 1     
            elif score_mat[i][0] == 2 and score_mat[i][1] == 2:
                assemble_scores[2][2] += 1     
            elif score_mat[i][0] == 2 and score_mat[i][1] == 3:
                assemble_scores[2][3] += 1     
            elif score_mat[i][0] == 2 and score_mat[i][1] == 4:
                assemble_scores[2][4] += 1
            elif score_mat[i][0] == 3 and score_mat[i][1] == 0:
                assemble_scores[3][0] += 1
            elif score_mat[i][0] == 3 and score_mat[i][1] == 1:
                assemble_scores[3][1] += 1     
            elif score_mat[i][0] == 3 and score_mat[i][1] == 2:
                assemble_scores[3][2] += 1     
            elif score_mat[i][0] == 3 and score_mat[i][1] == 3:
                assemble_scores[3][3] += 1     
            elif score_mat[i][0] == 3 and score_mat[i][1] == 4:
                assemble_scores[3][4] += 1            
            elif score_mat[i][0] == 4 and score_mat[i][1] == 0:
                assemble_scores[4][0] += 1
            elif score_mat[i][0] == 4 and score_mat[i][1] == 1:
                assemble_scores[4][1] += 1     
            elif score_mat[i][0] == 4 and score_mat[i][1] == 2:
                assemble_scores[4][2] += 1     
            elif score_mat[i][0] == 4 and score_mat[i][1] == 3:
                assemble_scores[4][3] += 1     
            elif score_mat[i][0] == 4 and score_mat[i][1] == 4:
                assemble_scores[4][4] += 1     
   
        print ("*--------------  SCORE MATRIX --------------  *")

        score_matrix = PrettyTable([" ", 0, 1, 2, 3, 4])
        score_matrix.add_row([0,round(assemble_scores[0][0]/num_simulations*100,2),round(assemble_scores[0][1]/num_simulations*100,2),round(assemble_scores[0][2]/num_simulations*100,2),round(assemble_scores[0][3]/num_simulations*100,2),round(assemble_scores[0][4]/num_simulations*100,2)])
        score_matrix.add_row([1,round(assemble_scores[1][0]/num_simulations*100,2),round(assemble_scores[1][1]/num_simulations*100,2),round(assemble_scores[1][2]/num_simulations*100,2),round(assemble_scores[1][3]/num_simulations*100,2),round(assemble_scores[1][4]/num_simulations*100,2)])
        score_matrix.add_row([2,round(assemble_scores[2][0]/num_simulations*100,2),round(assemble_scores[2][1]/num_simulations*100,2),round(assemble_scores[2][2]/num_simulations*100,2),round(assemble_scores[2][3]/num_simulations*100,2),round(assemble_scores[2][4]/num_simulations*100,2)])
        score_matrix.add_row([3,round(assemble_scores[3][0]/num_simulations*100,2),round(assemble_scores[3][1]/num_simulations*100,2),round(assemble_scores[3][2]/num_simulations*100,2),round(assemble_scores[3][3]/num_simulations*100,2),round(assemble_scores[3][4]/num_simulations*100,2)])
        score_matrix.add_row([4,round(assemble_scores[4][0]/num_simulations*100,2),round(assemble_scores[4][1]/num_simulations*100,2),round(assemble_scores[4][2]/num_simulations*100,2),round(assemble_scores[4][3]/num_simulations*100,2),round(assemble_scores[4][4]/num_simulations*100,2)])
        print(score_matrix) 
        
        home_xPts = (home_win_probability / 100) * 3.0 + (draw_probability / 100) * 1.0 + (away_win_probability / 100) * 0.0
        away_xPts = (away_win_probability / 100) * 3.0 + (draw_probability / 100) * 1.0 + (home_win_probability / 100) * 0.0
     
        print ("* -------------- SUMMARY -------------- *")

        print(input_home_team, "win probability %:", home_win_probability, "xPts =", round(home_xPts,2))
        print(input_away_team, "win probability %:", away_win_probability, "xPts =", round(away_xPts,2))
        print("Draw probability %:", draw_probability)
        

        result_tuple_csv = (input_home_team, round(home_win_probability,2), round(home_xPts,2), input_away_team, round(away_win_probability,2), round(away_xPts,2), "\n")
        final_results_filename = "MonteCarloMatchSimResults" + formatted_season + ".csv"
        with open(final_results_filename, "a+") as myfile:
            myfile.write(",".join(map(str, result_tuple_csv)))
            
        for team, xpts in ovl_xpts_dict.items():
            if team == input_home_team:
                ovl_xpts_dict.update({team: round((xpts + home_xPts),2)})
            elif team == input_away_team:
                ovl_xpts_dict.update({team: round((xpts + away_xPts),2)})
        for team, xgf in ovl_xgf_dict.items():
            if team == input_home_team:
                ovl_xgf_dict.update({team: round((xgf + input_home_team_xg),2)})
            elif team == input_away_team:
                ovl_xgf_dict.update({team: round((xgf + input_away_team_xg),2)})
        for team, xga in ovl_xga_dict.items():
            if team == input_home_team:
                ovl_xga_dict.update({team: round((xga + input_away_team_xg),2)})
            elif team == input_away_team:
                ovl_xga_dict.update({team: round((xga + input_home_team_xg),2)})
        for team, xgd in ovl_xgd_dict.items():
            if team == input_home_team:
                ovl_xgd_dict.update({team: round((xgd + (input_home_team_xg - input_away_team_xg)),2)})
            elif team == input_away_team:
                ovl_xgd_dict.update({team: round((xgd + (input_away_team_xg - input_home_team_xg)),2)})
else:
    print("Not a valid option. Exiting.")
    sys.exit()

if choice == "csv":
    # sort the xpts dictionary
    sorted_ovl_xpts_dict = sorted(ovl_xpts_dict.items(), key=lambda x:x[1], reverse=True)
    converted_ovl_xpts_dict = dict(sorted_ovl_xpts_dict)
    
    
    final_table = []
    rank = 0
    for team, xpts in converted_ovl_xpts_dict.items():
        xgf = round(ovl_xgf_dict.get(team),2)
        xga = round(ovl_xga_dict.get(team),2)
        xgd = round(ovl_xgd_dict.get(team),2)
        pts = round(points.get(team),2)
        ptsdiff = round((pts - xpts),2)
        rank += 1
        team_stats = [rank, team, round(xpts,2), pts, ptsdiff, xgf, xga, xgd]
        final_table.append(team_stats)


    final_table_manip = np.array([list(elem) for elem in final_table]).T.tolist()
    

    fig = go.Figure(data=[go.Table(
        header=dict(values=['<b>RANK</b>', '<b>TEAM</b>', '<b>XPTS</b>', '<b>PTS</b>', '<b>PTSDIFF</b>', '<b>XGF</b>', '<b>XGA</b>', '<b>XGD</b>'],
                    line_color='black',
                    fill_color='white',
                    align='center',
                    font_size=10,
                    font_color='black'),
        cells=dict(values=[list(elem) for elem in final_table_manip],
                line_color='black',
                fill_color='white',
                align='center',
                font_size=12)),
    ])

    fig_name = "Simulation_for" + formatted_season + ".html"
    fig.update_layout(width=1200, height=1000)
    fig.update_layout(
    title={
        'text': "<b>xPTS Table - Premier League Season " + season + "</b><br><sup><b>@Suhail Parker</b> </b></sup><br><sup>xG data from fbref.com | xPTS calculated after 20,000 Monte Carlo Simulations | https://github.com/deathek1d/</sup>",
        'y':0.95,
        'x':0.50,
        'xanchor': 'center',
        'yanchor': 'top',
        'font_size': 18})
    fig.write_html(fig_name)
