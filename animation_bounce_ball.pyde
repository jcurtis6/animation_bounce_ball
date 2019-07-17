ball_y = 100
ball_x = 50
y_speed = 3
x_speed = 3

def setup():    #runs once
    size(500,500)
    

def draw():   #runs multiple times (loops)
    background (141, 147, 158)
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    fill(67, 250, 12)
    ellipse(200, ball_y, 100, 100)
    line(0, 400, 500, 400)
    line(0, 500, 500, 500) #right side
    line(0, 0, 0, 500) #left side
    
   
    if ball_y > 350: 
        print("BOUNCE")
        y_speed = -y_speed
        
    if ball_y < 42:
        y_speed = -y_speed
        
    if ball_x < 500:
        x_speed = -3
    
    ball_y = ball_y + y_speed
    ball_x = ball_x + x_speed
    
    
