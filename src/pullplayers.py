"""
modify this script to generate dictionaries of player codes



"""
import pandas as pd



year = '2019'
ptype='pitchers'

teams = ['LAA', 'HOU', 'OAK', 'TOR', 'ATL', 'MIL', 'STL', 
         'CHC', 'ARI', 'LAD', 'SF', 'CLE', 'SEA', 'MIA', 
         'NYM', 'WSH', 'BAL', 'SD', 'PHI', 'PIT', 'TEX', 
         'TB', 'BOS', 'CIN', 'COL', 'KC', 'DET', 'MIN', 
         'CWS', 'NYY']

PlayerDict = {}

for team in teams:
    
    print(team)

    linkp='https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=&hfC=&hfSea='+year+'%7C&hfSit=&player_type=pitcher&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&team='+team+'&position=&hfRO=&home_road=&hfFlag=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name-event&sort_col=pitches&player_event_sort=api_p_release_speed&sort_order=desc&min_abs=0&type=details&'
    
    linkb='https://baseballsavant.mlb.com/statcast_search/csv?all=true&hfPT=&hfAB=&hfBBT=&hfPR=&hfZ=&stadium=&hfBBL=&hfNewZones=&hfGT=R%7C&hfC=&hfSea='+year+'%7C&hfSit=&player_type=batter&hfOuts=&opponent=&pitcher_throws=&batter_stands=&hfSA=&game_date_gt=&game_date_lt=&hfInfield=&team='+team+'&position=&hfOutfield=&hfRO=&home_road=&hfFlag=&hfPull=&metric_1=&hfInn=&min_pitches=0&min_results=0&group_by=name&sort_col=pitches&player_event_sort=h_launch_speed&sort_order=desc&min_pas=0&type=details&'
    
    if ptype=='pitchers':
        df = pd.read_csv(linkp, low_memory=False)
        
        for indx,pname in enumerate(df.player_name):
            PlayerDict[pname] = df.pitcher[indx]
    else:
        df = pd.read_csv(linkb, low_memory=False)
        
        for indx,pname in enumerate(df.player_name):
            PlayerDict[pname] = df.batter[indx]
            
            

f = open('../data/playerdict'+year+'.txt','w')

print('Player,Key',file=f)

for indx,val in enumerate(PlayerDict.values()):
    print(list(PlayerDict.keys())[indx],',',list(PlayerDict.values())[indx],file=f)
    
f.close()

