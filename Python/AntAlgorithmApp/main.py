from varibles import *
from Graph2d import *
from Graph2dVisual import *
from UIClasses import *
from AntAlgorithm import *



def FillWindow(surface,color):
    surface.fill(color)


def DrawRect(surface,pos,size,color,border=False):
    rect = pygame.Rect(pos, np.array(pos)+np.array(size))
    pygame.draw.rect(surface=surface,
                     rect=(pos[0],pos[1],size[0],size[1]),
                     color=color,
                     width=border)
    return rect

def DrawLine(surface,start,end,color,width):
    rect = pygame.Rect(start,np.array(end)-np.array(start))
    pygame.draw.line(surface=surface,
                     color=color,
                     start_pos=rect.topleft,
                     end_pos=rect.bottomright,
                     width=width)
    return rect

def DrawCircle(surface,pos,radius,color,border=False):
    rect = pygame.Rect(np.array(pos)-radius,(2*radius,2*radius))
    pygame.draw.circle(surface=surface,
                       color=color,
                       center=rect.center,
                       radius=radius,
                       width=border)
    return rect

@jit(fastmath=True,parallel=True,forceobj=True,cache=True)
def Fade(surface):
    return  pygame.surfarray.make_surface((np.array(Image.fromarray(np.array(pygame.surfarray.array3d(surface)), mode='RGB')) * 0.9).astype('int'))


def Init():
    FillWindow(WIN,WIN_FILL_COLOR)

def main():
    appClock = pygame.time.Clock()

    isRun = True
    isMove=False

    selectedVertex2d,selectedVertex2dUI = None,None


    g2dv = Graph2dVisual()
    g2dv.CreateVerticies(3)

    g2dv.setVerticiesPosFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm_App(python)\graph.xlsx',0)
    g2dv.setLinksFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm_App(python)\graph.xlsx',1)
    g2dv.setWeightsFromExcel(f'F:\From Disk Windows 7 SSD\PyCharm Projects\GeneralProject\AntAlgorithm_App(python)\graph.xlsx',2)

    g2dv.init()
    g2dv.upd()

    g2dv.Draw(WIN)


    while isRun:
        appClock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRun=False
            if event.type==pygame.MOUSEBUTTONDOWN:
                selectedVertex2d,selectedVertex2dUI =  g2dv.FindSelectedVertex(pygame.mouse.get_pos())
                if selectedVertex2dUI != None:
                    isMove=True

            elif event.type==pygame.MOUSEBUTTONUP:
                isMove=False
                selectedVertex2dUI=None
            elif event.type==pygame.MOUSEMOTION and isMove:
                FillWindow(WIN,WIN_FILL_COLOR)

                g2dv.updVertex(selectedVertex2d,selectedVertex2dUI,event.rel)
                g2dv.upd()
                g2dv.Draw(WIN)

        pygame.display.update(WIN)



    pygame.quit()





if __name__ == "__main__":
    Init()
    main()
