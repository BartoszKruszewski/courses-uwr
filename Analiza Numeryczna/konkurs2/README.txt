The program has been prepared for contest #2 in Numerical Analysis.

Both the curve editor and the text editor utilize multiple third-degree Bézier curves
with variable weights. This is a popular approach in contemporary font design,
providing a more convenient workflow than variable-degree curves.
In the editor, when adding a new curve, a new "end point" is added to it.
"Internal" points for modeling curvature are automatically added and displayed,
only when a specific curve is selected. Curves can be connected in "loops"
by moving the end point of one curve over the end point of another.
The weights of points on the curve can be changed by selecting the curve
and adjusting the scroll. This allows for easy achievement of "aggressive" curvature.
Both curve points and their weights are saved in a single JSON file.

Instructions for preparing const.py:
-   Set IMAGE_NAME to the name of the image to be displayed in the background.
-   Set BASE_COLOR, ACTIVE_COLOR, HELPER_COLOR, MASTER_COLOR, BACKGROUND_COLOR
    to maintain clarity when drawing curves.
-   If using a less powerful device, you can reduce the DRAW_PRECISION constant.
-   Set CURVE_NAME to the name of the file with the output of the obtained curves.

Instructions for drawing curves:
-   Left mouse button: create new curves connected to the previously selected point.
-   Right mouse button: select and move points.
-   Scroll: change the weight of a point.
-   Left Ctrl: create a new curve unconnected to the rest of the points.
-   Left Shift: change the preview.
-   Delete: delete the selected point.

Text editor instructions:
-   In the char_mapping file, specify which keys should be associated with, 
    which curve files and what their scale should be.
-   Delete: delete the next character.
-   Backspace: delete the previous character.
-   Enter: new line.
-   - = (next to backspace): change font size.
-   Left Ctrl: change font effect (normal, bold, italic).
-   Scroll: scroll through the entire text.
-   Arrows: navigate through characters.