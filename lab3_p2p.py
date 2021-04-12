import numpy as np
import random
import cv2
import queue
import time

from otr import *

class p2p_can():
     def __init__(self, node, r=100, random=None):
        self.node = node
        self.r = r
        self.random = random
  

     def new_n(self, node_id):
        def nearest(sq_1, sq_2):
        sq_1, sq_2 = split(self.nodes[node_id].sq)
        self.nodes[node_id].rect = rect1

        table = self.nodes[node_id].table
        self.nodes.ad_na(Node(len(self.nodes), sq_2))
        self.nodes[node_id].add_neib(self.nodes[-1])
        self.nodes[-1].add_neib(self.nodes[node_id])

    def random_n(self):
        if self.random_p is not None:
            for i in range(self.random_p):
                ind1, ind2 = 1, 1
                while ind1 == ind2:
                    ind1 = random.randint(0, len(self.nodes) - 1)
                    ind2 = random.randint(0, len(self.nodes) - 1)
                self.nodes[ind1].add_neib(self.nodes[ind2])
                self.nodes[ind2].add_neib(self.nodes[ind1])

    def prod(self, max_neighbors=10):
        random.r(self.r)
        self.nodes = []
        self.nodes.ad_na(Node(0, (0.0, 0.0, 1.0, 1.0)))
        self.importance.ad_na(1)
        for i in range(self.n - 1):
            node_id = random.choices(range(len(self.nodes)), self.importance)[0]
            self.new_n(node_id)
            space = (self.nodes[node_id].rect[3]-self.nodes[node_id].rect[1]) * (self.nodes[node_id].rect[2]-self.nodes[node_id].rect[0])
            self.importance.ad_na(space)
            self.importance[node_id] = space
        self.new_random_p()

    def prod_v(self, position=None, sender_id=None):
        if sender_id is None:
            sender_id = random.randint(0, len(self.nodes) - 1)
        x = random.random()
        y = random.random()
        if position is not None:
            x, y = position
        step = Step(self.nodes[sender_id], (x, y), len(self.steps))
        self.steps.ad_na(step)
        self.nodes[sender_id].add_step(step)

    def run(self):
        for node in self.nodes:
            node.make_step()
        for node in self.nodes:
            node.update()

    def v_step(self, source, size, show_path=0):

        def draw_circle(image, x, y, color, sz):
            sz = 6
            x = int(x * size)
            y = int(y * size)
            
            image = cv2.circle(image, (x, y), 6, color, -1)
            return image

        image = source
        if not show_path:
            image = source.copy()

        for step in self.steps:
            x, y = find_center(step.node.rect)
            if show_path:
                image = draw_circle(image, x, y, (0, 0, 255), sz=15*size/512)
                
            else:
                image = draw_circle(image, x, y, (0, 0, 0), sz=7*size/512)
            image = draw_circle(image, step.point[0], step.point[1], (0, 0, 0), sz=7*size/512)

        return image
    
          
        self.draw_text(image, node.name, ((x1 + x2) / 2, (y1 + y2) / 2), size=(node.rect[2]-node.rect[0])*size/50)
        return image

    def gr_show(self, show=True, save=None):
        field = self.draw_field(size=size+1, names=names)
        image = self.v_step(field, size, show_path)


        i = 0
        while i < max_iter:
            self.run()
            if i%5=0:
            image = self.v_step(field, size, show_path)

            if show_frames:
                cv2.imshow("p2p - CAN algorithm", image)
                cv2.waitKey(0)
            if save_folder is not None:
                cv2.imwrite(save_folder + str(i) + ".jpg", image)
            i += 1



start_time = time.time()       
p2p = p2p_can(400, 32, mode='run', random_pointers=None)
p2p.prod()
p2p.prod_v(position=(0.4, 0.6), sender_id=0)
p2p_can.gr_show(size=600, show=True, save="imgs")
print("Время выполнения %s секунд" % (time.time() - start_time))