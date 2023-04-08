import bpy
import math

# Создаем 4 кубика
for i in range(4):
    bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, location=(i*3, 0, 0))
    cube = bpy.context.object

    # Добавляем материалы
    material = bpy.data.materials.new(name=f"Material{i}")
    material.diffuse_color = (0.5, 0.5, 0.5, 1.0)
    cube.data.materials.append(material)

# Анимация каждого кубика
for i, obj in enumerate(bpy.context.scene.objects):
    if obj.type == 'MESH':
        # Устанавливаем кадры начала и конца анимации
        bpy.context.scene.frame_start = 0
        bpy.context.scene.frame_end = 100

        # Двигаем каждый кубик вдоль оси Y синусоидально
        for frame in range(bpy.context.scene.frame_start, bpy.context.scene.frame_end):
            # Вычисляем значение синусоиды для текущего кадра
            sin_value = math.sin((frame / 10) + i)

            # Устанавливаем позицию кубика на текущем кадре
            obj.location.y = sin_value

            # Добавляем ключевой кадр для позиции кубика
            obj.keyframe_insert(data_path='location', frame=frame)

