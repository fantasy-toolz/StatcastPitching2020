
# THIS WORKS!
import numpy as np
from skimage.measure import find_contours
from numpy.linalg import eig, inv


class SOEllipse(object):
    '''
    #
    # Conic Ellipse fitter
    #     exploiting the quadratic curve nature of the ellipse
    #

    advantages: fast

    disadvantages: does not have flexibility
    
    '''
    @staticmethod
    def fitEllipse(x,y):
        #
        # Take a set of x,y points at fit an ellipse to it
        #
        x = x[:,np.newaxis]
        y = y[:,np.newaxis]
        D =  np.hstack((x*x, x*y, y*y, x, y, np.ones_like(x)))
        S = np.dot(D.T,D)
        C = np.zeros([6,6])
        C[0,2] = C[2,0] = 2; C[1,1] = -1
        E, V =  eig(np.dot(inv(S), C))
        n = np.argmax(np.abs(E))
        a = V[:,n]
        
        return a
    @staticmethod
    def ellipse_center(a):
        b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
        num = b*b-a*c
        x0=(c*d-b*f)/num
        y0=(a*f-b*d)/num
            
        return np.array([x0,y0])
    @staticmethod
    def ellipse_angle_of_rotation( a ):
        b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
        
        return 0.5*np.arctan(2*b/(a-c))
    @staticmethod
    def ellipse_axis_length( a ):
        b,c,d,f,g,a = a[1]/2, a[2], a[3]/2, a[4]/2, a[5], a[0]
        up = 2*(a*f*f+c*d*d+g*b*b-2*b*d*f-a*c*g)
        down1=(b*b-a*c)*( (c-a)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
        down2=(b*b-a*c)*( (a-c)*np.sqrt(1+4*b*b/((a-c)*(a-c)))-(c+a))
        res1=np.sqrt(up/down1)
        res2=np.sqrt(up/down2)        
        return np.array([res1, res2])





def follow_contour(xx,yy,arr,level):
    
    dx = np.unique(xx[0,:])[1] - np.unique(xx[0,:])[0]
    xmin = np.min(np.unique(xx[0,:]))
    
    dy = np.unique(yy[:,0])[1] - np.unique(yy[:,0])[0]
    ymin = np.min(np.unique(yy[:,0]))
    
    res = find_contours(arr,level)
    
    #c = cntr.Cntr(xx,yy,arr)
    #res = c.trace(level)
    #
    xcon = []
    ycon = []
    try:
        for i in range(0,len(res[0])):
            xcon.append(dx*res[0][i][0] + xmin)
            ycon.append(dy*res[0][i][1] + ymin)
    except:
        print('No countour found at {}'.format(level))
        #
    XCON = np.array(xcon)
    YCON = np.array(ycon)
    return YCON,XCON


def make_ellipse(xcontours,ycontours):
    #
    # use parametric conic to get basic parameters
    #
    ell = SOEllipse.fitEllipse(xcontours,ycontours)
    phi = SOEllipse.ellipse_angle_of_rotation(ell)
    xcenter,ycenter = SOEllipse.ellipse_center(ell)
    alength = SOEllipse.ellipse_axis_length(ell)
    a = np.max(alength)
    b = np.min(alength)
    return a,b,phi,xcenter,ycenter







