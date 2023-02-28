import config
import numpy as np
import json,pickle


class BOOKING():
    def __init__(self,no_of_adults,no_of_children,no_of_weekend_nights, no_of_week_nights,type_of_meal_plan,required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type,repeated_guest,no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests):
        self.no_of_adults=no_of_adults
        self.no_of_children=no_of_children
        self.no_of_weekend_nights=no_of_weekend_nights
        self.no_of_week_nights=no_of_week_nights
        self.type_of_meal_plan=type_of_meal_plan
        self.required_car_parking_space=required_car_parking_space
        self.room_type_reserved=room_type_reserved
        self.lead_time=lead_time
        self.arrival_year=arrival_year
        self.arrival_month=arrival_month
        self.arrival_date=arrival_date
        self.market_segment_type=market_segment_type
        self.repeated_guest=repeated_guest
        self.no_of_previous_cancellations=no_of_previous_cancellations
        self.no_of_previous_bookings_not_canceled=no_of_previous_bookings_not_canceled
        self.avg_price_per_room=avg_price_per_room
        self.no_of_special_requests=no_of_special_requests
        
    def get_model(self):
        with open(config.modelpath,  "rb"  ) as f:
         self.model=pickle.load(f)  
        with open(config.jsonpath,"r") as f:
         self.json_data=json.load(f)  
    def get_predict(self):
        self.get_model()
        ar=np.zeros(len(self.json_data["columns"]),dtype=int) 
        ar[0]= self.no_of_adults
        ar[1]= self.no_of_children
        ar[2]= self.no_of_weekend_nights
        ar[3]= self.no_of_week_nights
        ar[4]= self.json_data["type_of_meal_plan"][self.type_of_meal_plan]
        ar[5]= self.required_car_parking_space
        ar[6]= self.json_data["room_type_reserved"][self.room_type_reserved]
        ar[7]=self.lead_time
        ar[8]= self.arrival_year
        ar[9]= self.arrival_month
        ar[10]= self.arrival_date
        ar[11]= self.json_data["market_segment_type"][self.market_segment_type]
        ar[12]=  self.repeated_guest
        ar[13]= self.no_of_previous_cancellations
        ar[14]= self.no_of_previous_bookings_not_canceled
        ar[15]= self.avg_price_per_room
        ar[16]= self.no_of_special_requests 
        # type_of_meal_plan=self.json_data["type_of_meal_plan"][self.type_of_meal_plan]
        # ar[14]=type_of_meal_plan
        # market_segment_type=self.json_data["market_segment_type"][self.market_segment_type]
        # ar[15]=market_segment_type
        # room_type_reserved=self.json_data["room_type_reserved"][self.room_type_reserved]
        # ar[16]=room_type_reserved
        
        print(ar)
        predictedprice=self.model.predict([ar])[0]
        return predictedprice
        
          
if __name__=="__main__" : 
    no_of_adults=                               2.00
    no_of_children=                             0.00
    no_of_weekend_nights =                      2.00
    no_of_week_nights=                          3.00
    type_of_meal_plan =                         "Meal_Plan1"
    required_car_parking_space=                 0.00
    room_type_reserved =                       "Room_Type1"
    lead_time =                                 5.00
    arrival_year =                           2018.00
    arrival_month=                             11.00
    arrival_date =                              6.00
    market_segment_type=                        'Offline'
    repeated_guest =                            0.00
    no_of_previous_cancellations=               0.00
    no_of_previous_bookings_not_canceled=       0.00
    avg_price_per_room=                       106.68
    no_of_special_requests=                     1.00  
    obj=BOOKING(no_of_adults,no_of_children,no_of_weekend_nights, no_of_week_nights,type_of_meal_plan,required_car_parking_space,room_type_reserved,lead_time,arrival_year,arrival_month,arrival_date,market_segment_type,repeated_guest,no_of_previous_cancellations,no_of_previous_bookings_not_canceled,avg_price_per_room,no_of_special_requests)  
    result=obj.get_predict() 
    print(result) 
                    
        
