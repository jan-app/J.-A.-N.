class Shapes():
    def triangle(base, height):
        area = (1 / 2) * base * height
        perimeter = "Sum of all sides"
        result = [float("{:.2f}".format(area)), perimeter]
        return result

    def equilateral_triangle(side):
        area = ((3 ** (1 / 2)) / 4) * side * side
        perimeter = 3 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def right_triangle(side1, side2):
        area = (side1 * side2) / 2
        hypotenuse = ((side1 * side1) + (side2 * side2)) ** (1 / 2)
        perimeter = side1 + side2 + hypotenuse
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter)), float("{:.2f}".format(hypotenuse))]
        return result

    def iso_triangle(base, height):
        area = (base * height)/2
        side = ((height * height) + ((base / 2) * (base / 2))) ** (1/2)
        perimeter = (2 * side) + base
        result = [("{:.2f}".format(area)), ("{:.2f}".format(perimeter)), ("{:.2f}".format(side))]
        return result

    def scal_triangle(side1, side2, side3):
        s = (side1 + side2 + side3) / 2
        area = (s * (s - side1) * (s - side2) * (s - side3)) ** (1 / 2)
        perimeter = s * 2
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def quad(diagnol1, dia1, dia2):
        area = ((1 / 2 * diagnol1 * dia1) + (1 / 2 * diagnol1 * dia2))
        perimeter = "Sum of all sides"
        result = [float("{:.2f}".format(area)), perimeter]
        return result

    def rectangle(lenght, width):
        area = lenght * width
        perimeter = 2 * (lenght + width)
        diagonal = ((lenght * lenght) + (width * width))**(1/2)
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter)), float("{:.2f}".format(diagonal))]
        return result

    def square(side):
        area = side * side
        perimeter = 4 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def rhombus(dia1, dia2):
        halfdia1 = dia1 / 2
        halfdia2 = dia2 / 2
        area = (dia1 * dia2) / 2
        perimeter = 2 * ((dia1 * dia1) + (dia2 * dia2)) ** (1 / 2)
        side = ((halfdia1 * halfdia1) + (halfdia2 * halfdia2)) ** (1 / 2)
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter)), float("{:.2f}".format(side))]
        return result

    def kite(dia1, dia2, side1, side2):
        area = (dia1 * dia2) / 2
        perimeter = 2 * (side1 + side2)
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def par_gm(side, base, height):
        area = base * height
        perimeter = 2 * (side + base)
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def trap(par1, par2, height, side1, side2):
        area = (1 / 2) * (par1 + par2) * height
        perimeter = par1 + par2 + side1 + side2
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def reg_pent(side):
        area = (1 / 4) * ((5 * (5 + 2 * (5 ** (1 / 2)))) ** (1 / 2)) * (side * side)
        perimeter = 5 * side
        diagnol = ((1 + (5 ** (1 / 2))) / 2) * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter)), float("{:.2f}".format(diagnol))]
        return result

    def reg_hex(side):
        area = ((3 * (3 ** (1 / 2))) / 2) * (side * side)
        perimeter = 6 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def reg_hept(side):
        area = (7 / 4) * (side * side) * 2.07652139657234
        perimeter = 7 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def reg_oct(side):
        area = 2 * (1 + (2 ** (1 / 2))) * (side * side)
        perimeter = 8 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def reg_nona(side):
        area = (9 / 4) * (side * side) * 2.74747741945462
        perimeter = 9 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def reg_deca(side):
        area = (5 / 2) * (side * side) * (5 + 2 * (5 ** (1 / 2))) ** (1 / 2)
        perimeter = 10 * side
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(perimeter))]
        return result

    def cir_acc(radius):
        area = (22 / 7) * radius * radius
        circumference = 2 * (22 / 7) * radius
        diameter = 2 * radius
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(circumference)), float("{:.2f}".format(diameter))]
        return result

    def cir_exc(radius):
        area = (3.141592653589793238) * radius * radius
        circumference = 2 * (3.141592653589793238) * radius
        diameter = 2 * radius
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(circumference)), float("{:.2f}".format(diameter))]
        return result

    def sm_cir_acc(radius):
        area = (1 / 2) * ((22 / 7) * (radius * radius))
        circumference = ((22 / 7) * radius) + (2 * radius)
        diameter = 2 * radius
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(circumference)), float("{:.2f}".format(diameter))]
        return result

    def sm_cir_exc(radius):
        area = (1 / 2) * ((3.141592653589793238) * (radius * radius))
        circumference = ((3.141592653589793238) * radius) + (2 * radius)
        diameter = 2 * radius
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(circumference)), float("{:.2f}".format(diameter))]
        return result

    def ell_acc(x, y):
        area = (22 / 7) * x * y
        circumference = (22 / 7) * (3 * (x + y) - (((3 * x + y) * (x + 3 * y)) ** (1 / 2)))
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(circumference))]
        return result

    def ell_exc(x, y):
        area = (3.141592653589793238) * x * y
        circumference = (3.141592653589793238) * (3 * (x + y) - (((3 * x + y) * (x + 3 * y)) ** (1 / 2)))
        result = [float("{:.2f}".format(area)), float("{:.2f}".format(circumference))]
        return result

    def cube(edge):
        volume = edge ** 3
        tsa = 6 * (edge * edge)
        lsa = 4 * (edge * edge)
        diagonal = (3 ** (1 / 2)) * edge
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa)),
                  float("{:.2f}".format(diagonal))]
        return result

    def cuboid(lenght, breadth, height):
        volume = lenght * breadth * height
        tsa = 2 * ((lenght * breadth) + (breadth * height) + (lenght * height))
        diagonal = ((lenght * lenght) + (breadth * breadth) + (height * height)) ** (1 / 2)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(diagonal))]
        return result

    def tri_prism(side1, side2, side3, height):
        s = ((side1 + side2 + side3) / 2)
        ar_base = ((s * (s - side1) * (s - side2) * (s - side3)) ** (1 / 2))
        volume = ar_base * height
        tsa = (2 * ar_base) + ((side1 + side2 + side3) * height)
        lsa = (side1 + side2 + side3) * height
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa)),
                  float("{:.2f}".format(ar_base))]
        return result

    def tri_pyramid(ar_base, pr_base, sl_height, height):
        volume = (1 / 3) * ar_base * height
        tsa = ar_base + ((1 / 2) * (pr_base * sl_height))
        lsa = (1 / 2) * (pr_base * sl_height)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa))]
        return result

    def sq_pyramid(side, height):
        volume = (side * side) * (height / 3)
        tsa = (side * side) + (2 * side) * (((side * side) / 4) + (height * height)) ** (1 / 2)
        lsa = side * ((side * side) + 4 * (height * height)) ** (1 / 2)
        ar_base = side * side
        ar_face = (side / 2) * (((side * side) / 4) + (height * height)) ** (1 / 2)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(ar_face))]
        return result

    def rect_pyramid(lenght, breadth, height):
        volume = (lenght * breadth * height) / 3
        tsa = (lenght * breadth) + lenght * ((((breadth / 2) ** 2) + (height * height)) ** (1 / 2)) + breadth * (
                    (((lenght / 2) ** 2) + (height * height)) ** (1 / 2))
        lsa = lenght * ((((breadth / 2) ** (2)) + (height * height)) ** (1 / 2)) + breadth * (
                    (((lenght / 2) ** (2)) + (height * height)) ** (1 / 2))
        ar_base = lenght * breadth
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa)),
                  float("{:.2f}".format(ar_base))]
        return result

    def pentagon_pyramid(side, height):
        s = 1.37638192047117
        volume = (5 / 12) * s * height * (side * side)
        tsa = (5 / 4) * s * (side * side) + (5 * (side / 2)) * ((height * height) + (((side * s) / 2) ** 2)) ** (1 / 2)
        lsa = (5 * side * ((height * height) + (((side * s) / 2) ** 2)) ** (1 / 2)) / 2
        ar_base = (5 / 4) * s * side * side
        ar_face = (side / 2) * ((height * height) + (((side * s) / 2) ** 2)) ** (1 / 2)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(ar_face))]
        return result

    def hexagon_pyramid(side, height):
        volume = ((3 ** (1 / 2)) / 2) * (side * side) * height
        tsa = ((3 * (3 ** (1 / 2))) / 2) * (side * side) + (3 * side) * (
                    (height * height) + ((3 * side * side) / 4)) ** (1 / 2)
        lsa = (3 * side) * ((height * height) + ((3 * side * side) / 4)) ** (1 / 2)
        ar_base = ((3 * (3 ** (1 / 2))) / 2) * (side * side)
        ar_face = (side / 2) * ((height * height) + ((3 * side * side) / 4)) ** (1 / 2)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(lsa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(ar_face))]
        return result

    def tetra_hedron(side):
        volume = (side * side * side) / (6 * (2 ** (1 / 2)))
        tsa = (3 ** (1 / 2)) * side * side
        ar_face = ((3 ** (1 / 2)) / 4) * side * side
        height = ((2 / 3) ** (1 / 2)) * side
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(ar_face)),
                  float("{:.2f}".format(height))]
        return result

    def octa_hedron(side):
        volume = ((2 ** (1 / 2)) / 3) * (side ** 3)
        tsa = 2 * (3 ** (1 / 2)) * side * side
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result

    def dodeca_hedron(side):
        volume = ((15 + 7 * (5 ** (1 / 2))) / 4) * (side * side * side)
        tsa = 3 * ((25 + 10 * ((5 ** (1 / 2)))) ** (1 / 2)) * side * side
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result

    def icosa_hedron(side):
        volume = ((5 * (3 + (5 ** (1 / 2)))) / 12) * (side * side * side)
        tsa = 5 * (3 ** (1 / 2)) * (side * side)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result

    def sphere_acc(radius):
        volume = (4 / 3) * (22 / 7) * (radius * radius * radius)
        tsa = 4 * (22 / 7) * (radius * radius)
        diameter = 2 * radius
        circumference = 2 * (22 / 7) * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(circumference)),
                  float("{:.2f}".format(diameter))]
        return result

    def sphere_exc(radius):
        volume = (4 / 3) * (3.141592653589793238) * (radius * radius * radius)
        tsa = 4 * (3.141592653589793238) * (radius * radius)
        diameter = 2 * radius
        circumference = 2 * (22 / 7) * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(circumference)),
                  float("{:.2f}".format(diameter))]
        return result

    def hemi_sphere_acc(radius):
        volume = (2 / 3) * (22 / 7) * (radius * radius * radius)
        tsa = 3 * (22 / 7) * (radius * radius)
        csa = 2 * (22 / 7) * radius * radius
        ar_base = (22 / 7) * radius * radius
        diameter = 2 * radius
        circumference = 2 * (22 / 7) * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(csa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(circumference)),
                  float("{:.2f}".format(diameter))]
        return result

    def hemi_sphere_exc(radius):
        volume = (2 / 3) * (3.141592653589793238) * (radius * radius * radius)
        tsa = 3 * (3.141592653589793238) * (radius * radius)
        csa = 2 * (3.141592653589793238) * radius * radius
        ar_base = (22 / 7) * radius * radius
        diameter = 2 * radius
        circumference = 2 * (3.141592653589793238) * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(csa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(circumference)),
                  float("{:.2f}".format(diameter))]
        return result

    def ellipsoid_acc(x, y, z):
        volume = (4 / 3) * (22 / 7) * x * y * z
        tsa = 4 * (22 / 7) * ((((x * y) ** (1.6)) + ((x * z) ** (1.6)) + ((y * z) ** (1.6))) / 3) ** (1 / 1.6)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result

    def ellipsoid_exc(x, y, z):
        volume = (4 / 3) * (3.141592653589793238) * x * y * z
        tsa = 4 * (3.141592653589793238) * ((((x * y) ** (1.6)) + ((x * z) ** (1.6)) + ((y * z) ** (1.6))) / 3) ** (
                    1 / 1.6)
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result

    def cylinder_acc(radius, height):
        volume = (22 / 7) * radius * radius * height
        tsa = (2 * (22 / 7) * radius * height) + (2 * (22 / 7) * radius * radius)
        csa = 2 * (22 / 7) * radius * height
        ar_base = (22 / 7) * radius * radius
        diameter = 2 * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(csa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(diameter))]
        return result

    def cylinder_exc(radius, height):
        volume = (3.141592653589793238) * radius * radius * height
        tsa = (2 * (3.141592653589793238) * radius * height) + (2 * (3.141592653589793238) * radius * radius)
        csa = 2 * (3.141592653589793238) * radius * height
        ar_base = (3.141592653589793238) * radius * radius
        diameter = 2 * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(csa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(diameter))]
        return result

    def cone_acc(radius, height):
        volume = (22 / 7) * radius * radius * (height / 3)
        tsa = (22 / 7) * radius * (radius + ((height * height) + (radius * radius)) ** (1 / 2))
        csa = (22 / 7) * radius * (((height * height) + (radius * radius)) ** (1 / 2))
        ar_base = (22 / 7) * radius * radius
        sl_height = ((radius * radius) + (height * height)) ** (1 / 2)
        diameter = 2 * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(csa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(sl_height)), float("{:.2f}".format(diameter))]
        return result

    def cone_exc(radius, height):
        volume = (3.141592653589793238) * radius * radius * (height / 3)
        tsa = (3.141592653589793238) * radius * (radius + ((height * height) + (radius * radius)) ** (1 / 2))
        csa = (3.141592653589793238) * radius * (((height * height) + (radius * radius)) ** (1 / 2))
        ar_base = (3.141592653589793238) * radius * radius
        sl_height = ((radius * radius) + (height * height)) ** (1 / 2)
        diameter = 2 * radius
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa)), float("{:.2f}".format(csa)),
                  float("{:.2f}".format(ar_base)), float("{:.2f}".format(sl_height)), float("{:.2f}".format(diameter))]
        return result

    def torus_acc(radius1, radius2):
        volume = 2 * ((22 / 7) ** 2) * radius1 * ((radius2) ** 2)
        tsa = 4 * ((22 / 7) ** 2) * radius1 * radius2
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result

    def torus_exc(radius1, radius2):
        volume = 2 * ((3.141592653589793238) ** 2) * radius1 * ((radius2) ** 2)
        tsa = 4 * ((3.141592653589793238) ** 2) * radius1 * radius2
        result = [float("{:.2f}".format(volume)), float("{:.2f}".format(tsa))]
        return result
