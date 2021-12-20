import pandas as pd
import seaborn as sns
import plotly.graph_objects as go
from numpy import transpose
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("data.csv")
# print(data['Dribbling'].describe())
data_float = data.select_dtypes(include="float64")
# print(data_float['Dribbling'].tolist().index(data_float['Dribbling'].max()))


def best_player_in_every_position_by_skills(skills_list):
    grp_by_position = data.groupby("Position")
    # print(list(grp_by_position.groups.keys()))
    rows = []

    for position, items in grp_by_position:
        row = []

        print(position + " :  " + str(len(items)))
        categories = skills_list
        for category in categories:
            sprint_speeds = items[category]
            player_names = items["Name"]
            index = sprint_speeds.tolist().index(sprint_speeds.max())
            player_name = player_names.tolist()[index]
            print(category + "==>" + player_name)
            row.append(player_name)
        rows.append(row)

        print("...........................................")
    """columns = []
    for i in range(len(rows)-1):
        column = []
        for j in rows:
            column.append(j[i])
        columns.append(column)"""
    # columns = [list(x) for x in zip(rows)]
    columns = transpose(rows)
    columns = np.insert(columns, 0, list(grp_by_position.groups.keys()), axis=0)

    skills_list = np.insert(skills_list, 0, "Position")

    fig = go.Figure(
        data=[go.Table(header=dict(values=skills_list), cells=dict(values=columns))]
    )
    fig.update_layout(
        title_text="Best Player From Each Position By Skills (Based on FIFA 2019 Ratings)"
    )
    fig.show()


def best_player_by_position():
    print("best players by position")
    skills_by_position = {
        "GK": {"GKDiving": 5, "GKReflexes": 5, "GKPositioning": 2, "GKKicking": 1},
        "CB": {
            "Interceptions": 5,
            "LongPassing": 4,
            "ShortPassing": 4,
            "SlidingTackle": 5,
            "StandingTackle": 5,
            "Strength": 3,
            "Marking": 3,
        },
        "LCB": {
            "Interceptions": 5,
            "LongPassing": 4,
            "ShortPassing": 4,
            "SlidingTackle": 5,
            "StandingTackle": 5,
            "Strength": 3,
            "Marking": 3,
        },
        "RCB": {
            "Interceptions": 5,
            "LongPassing": 4,
            "ShortPassing": 4,
            "SlidingTackle": 5,
            "StandingTackle": 5,
            "Strength": 3,
            "Marking": 3,
        },
        "CM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 5,
            "Stamina": 3,
            "BallControl": 4,
            "Positioning": 4,
            "Dribbling": 3,
            "Interceptions": 3,
            "StandingTackle": 3,
            "SlidingTackle": 3,
        },
        "CAM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 5,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 4,
            "LongShots": 4,
            "Acceleration": 3,
            "Volleys": 3,
            "Finishing": 3,
            "Aggression": 2,
        },
        "CDM": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Vision": 3,
            "Stamina": 3,
            "BallControl": 3,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
            "Marking": 5,
            "Strength": 3,
        },
        "LDM": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Vision": 3,
            "Stamina": 3,
            "BallControl": 3,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
            "Marking": 5,
            "Strength": 3,
        },
        "RDM": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Vision": 3,
            "Stamina": 3,
            "BallControl": 3,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
            "Marking": 5,
            "Strength": 3,
        },
        "LCM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 5,
            "Stamina": 3,
            "BallControl": 4,
            "Positioning": 4,
            "Dribbling": 3,
            "Interceptions": 3,
            "StandingTackle": 3,
            "SlidingTackle": 3,
        },
        "RCM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 5,
            "Stamina": 3,
            "BallControl": 4,
            "Positioning": 4,
            "Dribbling": 3,
            "Interceptions": 3,
            "StandingTackle": 3,
            "SlidingTackle": 3,
        },
        "LAM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 3,
            "Finishing": 3,
            "Aggression": 2,
        },
        "LM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 3,
            "Finishing": 3,
            "Aggression": 2,
        },
        "RM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 3,
            "Finishing": 3,
            "Aggression": 2,
        },
        "RAM": {
            "ShortPassing": 5,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 3,
            "Finishing": 3,
            "Aggression": 2,
        },
        "LB": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Stamina": 4,
            "BallControl": 5,
            "Dribbling": 4,
            "SprintSpeed": 5,
            "Acceleration": 4,
            "Volleys": 3,
            "Curve": 4,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
        },
        "RB": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Stamina": 4,
            "BallControl": 5,
            "Dribbling": 4,
            "SprintSpeed": 5,
            "Acceleration": 4,
            "Volleys": 3,
            "Curve": 4,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
        },
        "LWB": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Stamina": 4,
            "BallControl": 5,
            "Dribbling": 4,
            "SprintSpeed": 5,
            "Acceleration": 4,
            "Volleys": 3,
            "Curve": 4,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
        },
        "RWB": {
            "ShortPassing": 4,
            "LongPassing": 4,
            "Stamina": 4,
            "BallControl": 5,
            "Dribbling": 4,
            "SprintSpeed": 5,
            "Acceleration": 4,
            "Volleys": 3,
            "Curve": 4,
            "Interceptions": 5,
            "StandingTackle": 5,
            "SlidingTackle": 4,
        },
        "RW": {
            "ShortPassing": 3,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 3,
            "Curve": 4,
        },
        "LW": {
            "ShortPassing": 3,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 3,
            "Curve": 4,
        },
        "CF": {
            "ShortPassing": 3,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 5,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 5,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 5,
            "Strength": 4,
            "ShotPower": 3,
        },
        "ST": {
            "ShortPassing": 3,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 5,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 5,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 5,
            "Strength": 4,
            "ShotPower": 3,
        },
        "LF": {
            "ShortPassing": 3,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 3,
            "Curve": 4,
        },
        "RF": {
            "ShortPassing": 3,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 3,
            "Curve": 4,
        },
        "LS": {
            "ShortPassing": 3,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 3,
            "Curve": 4,
        },
        "RS": {
            "ShortPassing": 3,
            "LongPassing": 5,
            "Vision": 2,
            "Stamina": 3,
            "BallControl": 5,
            "Positioning": 3,
            "Dribbling": 5,
            "SprintSpeed": 5,
            "LongShots": 4,
            "Acceleration": 4,
            "Volleys": 4,
            "Finishing": 3,
            "Curve": 4,
        },
    }

    # print(data['Position'].unique())

    grp_by_position = data.groupby("Position")

    for position, items in grp_by_position:
        scores = []
        eval_data = skills_by_position[position]
        for i in range(len(items["Name"])):
            score = 0
            total_wt = 0
            for j in eval_data.keys():
                total_wt += eval_data[j]

                score += eval_data[j] * items[j].tolist()[i]
            score = score / total_wt
            scores.append(score)
        best = items["Name"].tolist()[scores.index(max(scores))]
        print(position + " : " + best)


best_player_by_position()


def clubs_positions_scores():
    print("Club and their Scores")
    top_clubs = [
        "FC Bayern München",
        "FC Barcelona",
        "Real Madrid",
        "Paris Saint-Germain",
        "Atlético Madrid",
        "Juventus",
        "Manchester City",
        "Manchester United",
        "Liverpool",
        "Tottenham Hotspur",
        "Chelsea",
    ]
    data_top_clubs = data.loc[data["Club"].isin(top_clubs)]

    grp_by_club = data_top_clubs.groupby("Club")

    attacking_pos = ["CF", "LW", "RW", "LF", "RF", "ST", "LS", "RS"]
    mid_pos = ["CAM", "LAM", "RAM", "LM", "RM", "CDM", "LDM", "RDM"]
    def_pos = ["CB", "LCB", "RCB", "LB", "RB", "WB", "LWB", "RWB", "GK"]

    attack_scores = []
    mid_scores = []
    def_scores = []

    scores = []
    clubs = []
    positions = []

    for club, items in grp_by_club:
        attack_score, mid_score, def_score = 0, 0, 0
        attackers, mids, defs = 0, 0, 0
        for row_num, row in items.iterrows():
            if row["Position"] in attacking_pos:
                attack_score += row["Overall"]
                attackers += 1
            elif row["Position"] in mid_pos:
                mid_score += row["Overall"]
                mids += 1
            elif row["Position"] in def_pos:
                def_score += row["Overall"]
                defs += 1

        attack_scores.append(attack_score / len(items["ID"]))
        print(club)
        print("Attack===>" + str(attack_score / attackers) + "(" + str(attackers) + ")")
        scores.append(attack_score / attackers)
        positions.append("Attack")
        clubs.append(club)

        print("Mid===>" + str(mid_score / mids) + "(" + str(mids) + ")")
        scores.append(mid_score / mids)
        positions.append("Mid")
        clubs.append(club)

        print("Defense===>" + str(def_score / defs) + "(" + str(defs) + ")")
        scores.append(def_score / defs)
        positions.append("Defense")
        clubs.append(club)
        print("....................................................")

        data_for_bar_plot = {"clubs": clubs, "positions": positions, "scores": scores}

    sns.barplot(x="clubs", y="scores", hue="positions", data=data_for_bar_plot)
    plt.xticks(rotation=70)

    plt.show()


clubs_positions_scores()


def clubs_players_age_analysis():
    top_clubs = [
        "FC Bayern München",
        "FC Barcelona",
        "Real Madrid",
        "Paris Saint-Germain",
        "Atlético Madrid",
        "Juventus",
        "Manchester City",
        "Manchester United",
        "Liverpool",
        "Tottenham Hotspur",
        "Chelsea",
    ]
    data_top_clubs = data.loc[data["Club"].isin(top_clubs)]
    grp_by_club = data_top_clubs.groupby("Club")
    clubs = []
    avg_ages = []
    for club, items in grp_by_club:
        avg_age = items["Age"].sum() / len(items["Age"])
        clubs.append(club)
        avg_ages.append(avg_age)
    graph = sns.barplot(
        x="club", y="avg_age", data={"club": clubs, "avg_age": avg_ages}
    )
    graph.axhline(data["Age"].mean())
    plt.ylabel("Average Age")
    plt.xticks(rotation=70)
    plt.show()


clubs_players_age_analysis()


def all_clubs_players_age():
    print("Club's players Average Age")
    grp_by_club = data.groupby("Club")
    clubs = []
    avg_ages = []
    for club, items in grp_by_club:
        clubs.append(club)
        avg_age = items["Age"].sum() / len(items["Age"])
        avg_ages.append(avg_age)

    print("==================================")

    for i in range(10):
        print(
            clubs[avg_ages.index(min(avg_ages))]
            + "=>"
            + str(avg_ages[avg_ages.index(min(avg_ages))])
        )
        clubs.pop(avg_ages.index(min(avg_ages)))
        avg_ages.pop(avg_ages.index(min(avg_ages)))


all_clubs_players_age()


"""

Index(['Unnamed: 0', 'ID', 'Name', 'Age', 'Photo', 'Nationality', 'Flag',
       'Overall', 'Potential', 'Club', 'Club Logo', 'Value', 'Wage', 'Special',
       'Preferred Foot', 'International Reputation', 'Weak Foot',
       'Skill Moves', 'Work Rate', 'Body Type', 'Real Face', 'Position',
       'Jersey Number', 'Joined', 'Loaned From', 'Contract Valid Until',
       'Height', 'Weight', 'LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW',
       'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM', 'LWB', 'LDM',
       'Finishing', 'HeadingAccuracy', 'ShortPassing', 'Volleys', 'Dribbling',
       'Curve', 'FKAccuracy', 'LongPassing', 'BallControl', 'Acceleration',
       'SprintSpeed', 'Agility', 'Reactions', 'Balance', 'ShotPower',
       'Jumping', 'Stamina', 'Strength', 'LongShots', 'Aggression',
       'Interceptions', 'Positioning', 'Vision', 'Penalties', 'Composure',
       'Marking', 'StandingTackle', 'SlidingTackle', 'GKDiving', 'GKHandling',
       'GKKicking', 'GKPositioning', 'GKReflexes', 'Release Clause'],
      dtype='object')

      """
