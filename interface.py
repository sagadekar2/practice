from flask import Flask
from flask import jsonify,request
from  utils import BOOKING
import config

app=Flask(__name__)
@app.route("/")
def get_homeapi():
    
    return "homeapi"

@app.route("/booking",methods=["GET","POST"])
def get_status(): 
    if request.method=="GET":
        data=request.form
        print(data)
        no_of_adults= eval(data["no_of_adults"])                              
        no_of_children=eval(data["no_of_children"])                             
        no_of_weekend_nights =eval(data["no_of_weekend_nights"])                      
        no_of_week_nights= eval(data["no_of_week_nights"])                          
        type_of_meal_plan =data["type_of_meal_plan"]                        
        required_car_parking_space=eval(data[" required_car_parking_space"])                
        room_type_reserved =data[" room_type_reserved"]                      
        lead_time =eval(data["lead_time"])                                
        arrival_year =eval(data["arrival_year"])                           
        arrival_month=eval(data["arrival_month"])                             
        arrival_date =eval(data["arrival_date"])                              
        market_segment_type=data[" market_segment_type"]                    
        repeated_guest = eval(data["repeated_guest"])                           
        no_of_previous_cancellations=eval(data["no_of_previous_cancellations"])               
        no_of_previous_bookings_not_canceled=eval(data["no_of_previous_bookings_not_cancele"])        
        avg_price_per_room=eval(data["avg_price_per_room"])                        
        no_of_special_requests=eval(data["no_of_special_requests"]) 
        print("hiiiii")
        obj=BOOKING(no_of_adults,no_of_children,no_of_weekend_nights, no_of_week_nights,type_of_meal_plan,required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type,repeated_guest,no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests)  
        result=obj.get_predict()  
        return jsonify({"result":result})  
    
    elif request.method=="POST":
        data=request.form
        print(data)
        no_of_adults= eval(data["no_of_adults"])                              
        no_of_children=eval(data["no_of_children"])                             
        no_of_weekend_nights =eval(data["no_of_weekend_nights"])                      
        no_of_week_nights= eval(data["no_of_week_nights"])                          
        type_of_meal_plan =data["type_of_meal_plan"]                         
        required_car_parking_space=eval(data[" required_car_parking_space"])                
        room_type_reserved =data[" room_type_reserved"]                      
        lead_time =eval(data["lead_time"])                                
        arrival_year =eval(data["arrival_year"])                           
        arrival_month=eval(data["arrival_month"])                             
        arrival_date =eval(data["arrival_date"])                              
        market_segment_type=data[" market_segment_type"]                     
        repeated_guest = eval(data["repeated_guest"])                           
        no_of_previous_cancellations=eval(data["no_of_previous_cancellations"])               
        no_of_previous_bookings_not_canceled=eval(data["no_of_previous_bookings_not_cancele"])        
        avg_price_per_room=eval(data["avg_price_per_room"])                        
        no_of_special_requests=eval(data["no_of_special_requests"]) 
        
        obj=BOOKING(no_of_adults,no_of_children,no_of_weekend_nights, no_of_week_nights,type_of_meal_plan,required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type,repeated_guest,no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests)  
        result=obj.get_predict()  
        return jsonify({"result":result})  
    
if __name__=="__main__" :
    app.run(port=config.port_no)          
    

    
