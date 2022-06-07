import arcade

arcade.open_window(600, 600, "drawing")

#arcade.set_background_color((48, 186, 143))
arcade.set_background_color(arcade.color.CARIBBEAN_GREEN)



arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.color.TEAL)

arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_ellipse_filled(100, 370, 60, 80, arcade.csscolor.DARK_GREEN)

arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
arcade.draw_polygon_filled(((500, 400),
                            (480, 360),
                            (470, 320),
                            (530, 320),
                            (520, 360)
                            ),
                           arcade.csscolor.DARK_GREEN)

arcade.finish_render()

arcade.run()