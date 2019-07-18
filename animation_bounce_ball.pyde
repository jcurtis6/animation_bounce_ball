ball_y = 100
ball_x = 50
y_speed = 5
x_speed = 5
mouse_x = 0
mouse_y = 400
block1 = True
block2 = True

def setup():    #runs once
    size(500,500)
    

def draw():   #runs multiple times (loops)
    background (141, 147, 158)
    global ball_y
    global y_speed
    global ball_x
    global x_speed
    global rect_x
    global rect_y
    global block1
    global block2
    fill(67, 250, 12)
    ellipse(ball_x, ball_y, 50, 50)
    line(0, 400, 500, 400)
    line(0, 500, 500, 500) #right side
    line(0, 0, 0, 500) #left side
    rect(mouseX,395, 100, 25)
    
    
    fill(141, 12, 36) #Color 2
    rect(100, 0, 100, 25)
    fill(200, 78, 98) #Color 3
    rect(200, 0, 100, 25)
    fill(66, 135, 245) #Color 4
    rect(300, 0, 100, 25)
    fill(245, 227, 66) #Color 5
    rect(400, 0, 100, 25)
    
    
    if ball_y > 370 and ball_x > mouseX and ball_x < mouseX + 100 and ball_y < 395: 
        print("BOUNCE")
        y_speed = -y_speed
        
    if ball_y < 42:
        y_speed = -y_speed
    
    if ball_x > 500:
        x_speed =-x_speed
   
    if ball_x < 0:
        x_speed = -x_speed
        print("die")
        
    if ball_x > 0 and ball_x < 100 and ball_y > 0 and ball_y < 50:  #Block 1
        block1 = False
    
    if block1:
        rect(0, 0, 100, 25)
    
   
    
        
        
    
      
     
     
    
    
    ball_y = ball_y + y_speed
    ball_x = ball_x + x_speed
    
    
