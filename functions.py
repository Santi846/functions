import numpy as np;
import matplotlib.pyplot as mplib;

x = np.linspace(0,6,100);
y = np.sin(x);

mplib.plot(x,y,label="y=sin(x)");


mplib.xlabel('x');
mplib.ylabel('y');
mplib.title("Check the function");
mplib.xticks(np.arange(0,6,2));
mplib.yticks(np.arange(-1,2,1));

mplib.show();