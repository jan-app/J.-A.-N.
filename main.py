from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivymd.app import MDApp
from important import Shapes
from kivymd.uix.snackbar import Snackbar

Window.size = (290, 580)

def snackbarforinput():
    Snackbar(text="[color=#ff6961]Please fill the all the required blanks[/color]",).open()
def snackbar_for_pie():
    Snackbar(text="[color=#ff6961]Please select value of pi[/color]",).open()
class MainScreen(Screen):
    pass

class TriangleWindow(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        try:
            base_input = float(base_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if base_input != '' and height_input != '':
            answer = Shapes.triangle(base_input, height_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
        
class EquilateralTriangleWindow(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        try:
            base_input = float(base_input) #  #FF3030 #ddbb34 #ff6961
        except ValueError:
            snackbarforinput()
        if base_input != '':
            answer = Shapes.equilateral_triangle(float(base_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
        
class RightTriangleWindow(Screen):
    def queans(self):
        side1_input = self.ids.side1_value.text
        side2_input = self.ids.side2_value.text
        try:
            side1_input = float(side1_input)
            side2_input = float(side2_input)
        except ValueError:
            snackbarforinput()
        if side1_input != '' and side2_input != '':
            answer = Shapes.right_triangle(float(side1_input), float(side2_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.hypotenuse_value.hint_text = str(answer[2])

class IsoscelesTriangleWindow(Screen):
    def queans(self):
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        try:
            base_input = float(base_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if base_input != '' and height_input != '':
            answer = Shapes.iso_triangle(float(base_input), float(height_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.side_value.hint_text = str(answer[2])
        
class ScaleneTriangleWindow(Screen):
    def queans(self):
        side1_input = self.ids.side1_value.text
        side2_input = self.ids.side2_value.text
        side3_input = self.ids.side3_value.text
        try: 
            side1_input = float(side1_input)
            side2_input = float(side2_input)
            side3_input = float(side3_input)
        except ValueError:
            snackbarforinput()
        if side1_input != '' and side2_input != '' and side3_input != '':
            answer = Shapes.scal_triangle(float(side1_input), float(side2_input), float(side3_input))
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            
class QuadrilateralWindow(Screen):
    def queans(self):
        large_dia_input = self.ids.large_dia_value.text
        small_dia_1_input = self.ids.small_dia_1_value.text
        small_dia_2_input = self.ids.small_dia_2_value.text
        try:
            large_dia_input = float(large_dia_input)
            small_dia_1_input = float(small_dia_1_input)
            small_dia_2_input = float(small_dia_2_input)
        except ValueError:
            snackbarforinput()    
        if large_dia_input != '' and small_dia_1_input != '' and small_dia_2_input != '':
            answer = Shapes.quad(large_dia_input, small_dia_1_input, small_dia_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            
class RectangleWindow(Screen):
    def queans(self):
        lenght_input = self.ids.lenght_value.text
        width_input = self.ids.width_value.text
        try: 
            lenght_input = float(lenght_input)
            width_input = float(width_input)
        except ValueError:
            snackbarforinput()
        if lenght_input != '' and width_input != '':
            answer = Shapes.rectangle(lenght_input, width_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.diagonal_value.hint_text = str(answer[2])
        
class SquareWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.square(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            
class RhombusWindow(Screen):
    def queans(self):
        dia_1_input = self.ids.dia_1_value.text
        dia_2_input = self.ids.dia_2_value.text
        try: 
            dia_1_input = float(dia_1_input)
            dia_2_input = float(dia_2_input)
        except ValueError:
            snackbarforinput()
        if dia_1_input != '' and dia_2_input != '':
            answer = Shapes.rhombus(dia_1_input, dia_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.side_value.hint_text = str(answer[2])
            
class KiteWindow(Screen):
    def queans(self):
        dia_1_input = self.ids.dia_1_value.text
        dia_2_input = self.ids.dia_2_value.text
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        try: 
            dia_1_input = float(dia_1_input)
            dia_2_input = float(dia_2_input)
            side_1_input = float(side_1_input)
            side_2_input = float(side_2_input)
        except ValueError:
            snackbarforinput()
        if dia_1_input != '' and dia_2_input != '' and side_1_input != '' and side_2_input != '':
            answer = Shapes.kite(dia_1_input, dia_2_input, side_1_input , side_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class ParallelogramWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        base_input = self.ids.base_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            base_input = float(base_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and base_input != '' and height_input != '':
            answer = Shapes.par_gm(side_input, base_input, height_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class TrapeziumWindow(Screen):
    def queans(self):
        par_1_input = self.ids.par_1_value.text
        par_2_input = self.ids.par_2_value.text
        height_input = self.ids.height_value.text
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        try: 
            par_1_input = float(par_1_input)
            par_2_input = float(par_2_input)
            height_input = float(height_input)
            side_1_input = float(side_1_input)
            side_2_input = float(side_2_input)
        except ValueError:
            snackbarforinput()
        if par_1_input != '' and par_2_input != '' and height_input !='' and side_1_input != '' and side_2_input != '':
            answer = Shapes.trap(par_1_input, par_2_input, height_input, side_1_input , side_2_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularPentagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_pent(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
            self.ids.diagonal_value.hint_text = str(answer[2])
    
class RegularHexagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_hex(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularHeptagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_hept(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])

class RegularOctagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_oct(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularNonagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_nona(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class RegularDecagonWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.reg_deca(side_input)
            self.ids.area_value.hint_text = str(answer[0])
            self.ids.perimeter_value.hint_text = str(answer[1])
    
class CircleWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_cir
        hival = pi_value
        pi_for_cir = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_cir == "22/7":
                    answer = Shapes.cir_acc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                elif pi_for_cir == "3.141":
                    answer = Shapes.cir_exc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class SemiCircleWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_sm_cir
        hival = pi_value
        pi_for_sm_cir = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_sm_cir == "22/7":
                    answer = Shapes.sm_cir_acc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                elif pi_for_sm_cir == "3.141":
                    answer = Shapes.sm_cir_exc(radius_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.perimeter_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class EllipseWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_ellipse
        hival = pi_value
        pi_for_ellipse = hival
    def queans(self):
        x_input = self.ids.x_value.text
        y_input = self.ids.y_value.text
        try: 
            x_input = float(x_input)
            y_input = float(y_input)
        except ValueError:
            snackbarforinput()
        if x_input != '' and y_input != '':
            try:
                if pi_for_ellipse == "22/7":
                    answer = Shapes.ell_acc(x_input, y_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.circumference_value.hint_text = str(answer[1])
                elif pi_for_ellipse == "3.141":
                    answer = Shapes.ell_exc(x_input, y_input)
                    self.ids.area_value.hint_text = str(answer[0])
                    self.ids.circumference_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class CubeWindow(Screen):
    def queans(self):
        edge_input = self.ids.edge_value.text
        try: 
            edge_input = float(edge_input)
        except ValueError:
            snackbarforinput()
        if edge_input != '':
            answer = Shapes.cube(edge_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.diagonal_value.hint_text = str(answer[3])
            
class CuboidWindow(Screen):
    def queans(self):
        length_input = self.ids.length_value.text
        breadth_input = self.ids.breath_value.text
        height_input = self.ids.height_value.text
        try: 
            length_input = float(length_input)
            breadth_input = float(breadth_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if length_input != '' and breadth_input != '' and height_input != '':
            answer = Shapes.cuboid(length_input, breadth_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.diagonal_value.hint_text = str(answer[2])
            
class TriangularPrismWindow(Screen):
    def queans(self):
        side_1_input = self.ids.side_1_value.text
        side_2_input = self.ids.side_2_value.text
        side_3_input = self.ids.side_3_value.text
        height_input = self.ids.height_value.text
        try: 
            side_1_input = float(side_1_input)
            side_2_input = float(side_2_input)
            side_3_input = float(side_3_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_1_input != '' and side_2_input != '' and side_3_input !='' and height_input != '':
            answer = Shapes.tri_prism(side_1_input, side_2_input, side_3_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            
class TriangularPyramidWindow(Screen):
    def queans(self):
        ar_base_input = self.ids.ar_base_value.text
        pr_base_input = self.ids.pr_base_value.text
        sl_height_input = self.ids.sl_height_value.text
        height_input = self.ids.height_value.text
        try: 
            ar_base_input = float(ar_base_input)
            pr_base_input = float(pr_base_input)
            sl_height_input = float(sl_height_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if ar_base_input != '' and pr_base_input != '' and sl_height_input !='' and height_input != '':
            answer = Shapes.tri_pyramid(ar_base_input, pr_base_input, sl_height_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            
class SquarePyramidWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and height_input != '':
            answer = Shapes.sq_pyramid(side_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            self.ids.ar_face_value.hint_text = str(answer[4])
            
class RectanglePyramidWindow(Screen):
    def queans(self):
        length_input = self.ids.length_value.text
        breadth_input = self.ids.breath_value.text
        height_input = self.ids.height_value.text
        try: 
            length_input = float(length_input)
            breadth_input = float(breadth_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if length_input != '' and breadth_input != '' and height_input != '':
            answer = Shapes.rect_pyramid(length_input, breadth_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            
class PentagonalPyramidWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and height_input != '':
            answer = Shapes.pentagon_pyramid(side_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            self.ids.ar_face_value.hint_text = str(answer[4])
            
class HexagonalPyramidWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        height_input = self.ids.height_value.text
        try: 
            side_input = float(side_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if side_input != '' and height_input != '':
            answer = Shapes.hexagon_pyramid(side_input, height_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.lsa_value.hint_text = str(answer[2])
            self.ids.ar_base_value.hint_text = str(answer[3])
            self.ids.ar_face_value.hint_text = str(answer[4])
            
class TetrahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.tetra_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            self.ids.ar_face_value.hint_text = str(answer[2])
            self.ids.height_value.hint_text = str(answer[3])
            
class OctahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.octa_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            
class DodecahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.dodeca_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            
class IcosahedronWindow(Screen):
    def queans(self):
        side_input = self.ids.side_value.text
        try: 
            side_input = float(side_input)
        except ValueError:
            snackbarforinput()
        if side_input != '':
            answer = Shapes.icosa_hedron(side_input)
            self.ids.volume_value.hint_text = str(answer[0])
            self.ids.tsa_value.hint_text = str(answer[1])
            
class SphereWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_sph
        hival = pi_value
        pi_for_sph = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_sph == "22/7":
                    answer = Shapes.sphere_acc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.circumference_value.hint_text = str(answer[2])
                    self.ids.diameter_value.hint_text = str(answer[3])
                elif pi_for_sph == "3.141":
                    answer = Shapes.sphere_exc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.circumference_value.hint_text = str(answer[2])
                    self.ids.diameter_value.hint_text = str(answer[3])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class HemiSphereWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_hm_sph
        hival = pi_value
        pi_for_hm_sph = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        try: 
            radius_input = float(radius_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '':
            try:
                if pi_for_hm_sph == "22/7":
                    answer = Shapes.hemi_sphere_acc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.circumference_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                elif pi_for_hm_sph == "3.141":
                    answer = Shapes.hemi_sphere_exc(radius_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.circumference_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
    
class EllipsoidWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_ellipsoid
        hival = pi_value
        pi_for_ellipsoid = hival
    def queans(self):
        x_input = self.ids.x_value.text
        y_input = self.ids.y_value.text
        z_input = self.ids.z_value.text
        try: 
            x_input = float(x_input)
            y_input = float(y_input)
            z_input = float(z_input)
        except ValueError:
            snackbarforinput()
        if x_input != '' and y_input != '' and z_input != '':
            try:
                if pi_for_ellipsoid == "22/7":
                    answer = Shapes.ellipsoid_acc(x_input, y_input, z_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                elif pi_for_ellipsoid == "3.141":
                    answer = Shapes.ellipsoid_exc(x_input, y_input, z_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class CylinderWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_cill
        hival = pi_value
        pi_for_cill = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        height_input = self.ids.height_value.text
        try: 
            radius_input = float(radius_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '' and height_input != '' :
            try:
                if pi_for_cill == "22/7":
                    answer = Shapes.cylinder_acc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.diameter_value.hint_text = str(answer[4])
                elif pi_for_cill == "3.141":
                    answer = Shapes.cylinder_exc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.diameter_value.hint_text = str(answer[4])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class ConeWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_cone
        hival = pi_value
        pi_for_cone = hival
    def queans(self):
        radius_input = self.ids.radius_value.text
        height_input = self.ids.height_value.text
        try: 
            radius_input = float(radius_input)
            height_input = float(height_input)
        except ValueError:
            snackbarforinput()
        if radius_input != '' and height_input != '' :
            try:
                if pi_for_cone == "22/7":
                    answer = Shapes.cone_acc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.slant_height_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                elif pi_for_cone == "3.141":
                    answer = Shapes.cone_exc(radius_input, height_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                    self.ids.csa_value.hint_text = str(answer[2])
                    self.ids.ar_base_value.hint_text = str(answer[3])
                    self.ids.slant_height_value.hint_text = str(answer[4])
                    self.ids.diameter_value.hint_text = str(answer[5])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class TorusWindow(Screen):
    def pi(smt,pi_value):
        global pi_for_tor
        hival = pi_value
        pi_for_tor = hival
    def queans(self):
        radius_1_input = self.ids.radius_1_value.text
        radius_2_input = self.ids.radius_2_value.text
        try: 
            radius_1_input = float(radius_1_input)
            radius_2_input = float(radius_2_input)
        except ValueError:
            snackbarforinput()
        if radius_1_input != '' and radius_2_input!= '':
            try:
                if pi_for_tor == "22/7":
                    answer = Shapes.torus_acc(radius_1_input, radius_2_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                elif pi_for_tor == "3.141":
                    answer = Shapes.torus_exc(radius_1_input, radius_2_input)
                    self.ids.volume_value.hint_text = str(answer[0])
                    self.ids.tsa_value.hint_text = str(answer[1])
                else:
                    snackbar_for_pie()
            except NameError:
                snackbar_for_pie()
            
class AboutUsWindow(Screen):
    pass


class MyScreenManager(ScreenManager):
    def change_screen_for_recent_to_main(self, screen):
        self.current = screen
        self.transition.direction = "up"
    def change_screen_for_recent(self, screen):
        self.current = screen  # the same as in .kv: app.root.current = screen
        self.transition.direction= "down"
    def change_screen_for_shapes(self, screen):
        self.current = screen  # the same as in .kv: app.root.current = screen
        self.transition.direction= "right"
        #self.transition = SwapTransition()

        
class TestApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = 'DeepPurple'
        self.theme_cls.primary_hue = '50'   ##Pentagrammic prism
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.accent_palette = 'Blue'
        self.icon = 'G:\code\Python 3.8.5 - 64bit\successful\J.A.N\LOGO\LOG12 LIGHT.png'
        

TestApp().run()
