from config.paths_config import *
from utils.helpers import *

def hybrid_recommendation(user_id, user_weight=0.5, content_weight=0.5):
    # User Recommendation
    similar_users = find_similar_users(user_id,USER_WEIGHTS,USER2USER_ENCODED,USER2USER_DECODED)
    user_pref = get_user_preferences(user_id,RATING_DF, ANIME_DF)
    user_recommended_animes=get_user_recommendation(similar_users, user_pref, ANIME_DF, RATING_DF, SYNOPSIS_DF)
    
    user_recommended_anime_list=user_recommended_animes["anime_name"].tolist()
    
    # Content Recommendation
    content_recommended_animes = []
    
    for anime in user_recommended_anime_list:
        similar_anime=find_similar_animes(anime,ANIME_WEIGHTS,ANIME2ANIME_ENCODED,ANIME2ANIME_DECODED,ANIME_DF)
        
        if similar_anime is not None and not similar_anime.empty:
            content_recommended_animes.extend(similar_anime["name"].tolist())
            
        else:
            print(f"No similar animes found for {anime}")
     
    combined_scores = {}
    
    for anime in user_recommended_anime_list:
        combined_scores[anime] = combined_scores.get(anime,0) + user_weight   
        
    for anime in user_recommended_anime_list:
        combined_scores[anime] = combined_scores.get(anime,0) + content_weight
        
    sorted_animes = sorted(combined_scores.items(), key=lambda x:x[1], reverse=True)
    
    return [anime for anime, score in sorted_animes[:10]]
    
    
    
    