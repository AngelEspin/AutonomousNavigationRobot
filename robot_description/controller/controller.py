#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
import argparse

# Inicializa el nodo
rospy.init_node('wheel_controller')

# Publicadores para los controladores de esfuerzo de velocidad
pub_j1 = rospy.Publisher('/robot/joint1_velocity_effort_controller/command', Float64, queue_size=10)
pub_j2 = rospy.Publisher('/robot/joint2_velocity_effort_controller/command', Float64, queue_size=10)
pub_j3 = rospy.Publisher('/robot/joint3_velocity_effort_controller/command', Float64, queue_size=10)
pub_j4 = rospy.Publisher('/robot/joint4_velocity_effort_controller/command', Float64, queue_size=10)
pub_j5 = rospy.Publisher('/robot/joint5_velocity_effort_controller/command', Float64, queue_size=10)
pub_j6 = rospy.Publisher('/robot/joint6_velocity_effort_controller/command', Float64, queue_size=10)

# Función para mover todas las ruedas hacia adelante
def move_forward_all_wheels():
    speed = Float64(1.0)  # Velocidad positiva
    pub_j1.publish(speed)
    pub_j2.publish(speed)
    pub_j3.publish(speed)
    pub_j4.publish(speed)
    pub_j5.publish(speed)
    pub_j6.publish(speed)

# Función para mover todas las ruedas hacia atrás
def move_backward_all_wheels():
    speed = Float64(-4.0)  # Velocidad negativa
    pub_j1.publish(speed)
    pub_j2.publish(speed)
    pub_j3.publish(speed)
    pub_j4.publish(speed)
    pub_j5.publish(speed)
    pub_j6.publish(speed)

# Función para mover R3 y R4 hacia atrás mientras las otras ruedas están quietas
def move_r3_r4_backward():
    speed_r3_r4 = Float64(-1.0)  # Velocidad negativa para R3 y R4
    stop_speed = Float64(0.0)  # Detener las otras ruedas
    pub_j1.publish(stop_speed)
    pub_j2.publish(stop_speed)
    pub_j3.publish(speed_r3_r4)
    pub_j4.publish(speed_r3_r4)
    pub_j5.publish(stop_speed)
    pub_j6.publish(stop_speed)

# Función para mover R3 y R4 hacia adelante
def move_r3_r4_forward():
    speed_r3_r4 = Float64(1.0)  # Velocidad positiva para R3 y R4
    stop_speed = Float64(0.0)  # Detener las otras ruedas
    pub_j1.publish(stop_speed)
    pub_j2.publish(stop_speed)
    pub_j3.publish(speed_r3_r4)
    pub_j4.publish(speed_r3_r4)
    pub_j5.publish(stop_speed)
    pub_j6.publish(stop_speed)

# Función para mover R1 y R2 hacia adelante
def move_r1_r2_forward():
    speed_r1_r2 = Float64(1.0)  # Velocidad positiva para R1 y R2
    stop_speed = Float64(0.0)  # Detener las otras ruedas
    pub_j1.publish(speed_r1_r2)
    pub_j2.publish(speed_r1_r2)
    pub_j3.publish(stop_speed)
    pub_j4.publish(stop_speed)
    pub_j5.publish(stop_speed)
    pub_j6.publish(stop_speed)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Controlador de ruedas del robot.')
    parser.add_argument('command', choices=['forward_all', 'backward_all', 'r3_r4_backward', 'r3_r4_forward', 'r1_r2_forward'],
                        help='El comando a ejecutar.')
    args = parser.parse_args()

    try:
        # Tiempo de espera para asegurar que los nodos están completamente inicializados
        rospy.sleep(1)

        if args.command == 'forward_all':
            move_forward_all_wheels()
        elif args.command == 'backward_all':
            move_backward_all_wheels()
        elif args.command == 'r3_r4_backward':
            move_r3_r4_backward()
        elif args.command == 'r3_r4_forward':
            move_r3_r4_forward()
        elif args.command == 'r1_r2_forward':
            move_r1_r2_forward()
        
        # Mantener el nodo vivo por un tiempo para asegurar que los comandos se envían
        rospy.sleep(5)

    except rospy.ROSInterruptException:
        pass