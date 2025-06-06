import cadquery as cq

result = None

part_0_0 = cq.Workplane('XY').box(1319.97, 301.66, 1292.43)
part_0_0 = part_0_0.translate((40.62, 16.50, 26.74))

result = part_0_0
part_0_1 = cq.Workplane('XY').box(1382.01, 292.33, 1244.53)
part_0_1 = part_0_1.translate((232.88, 567.59, -111.82))

result = result.union(part_0_1)
part_0_2 = cq.Workplane('XY').box(1396.52, 173.71, 1327.30)
part_0_2 = part_0_2.translate((-197.42, 1312.49, -147.40))

result = result.union(part_0_2)
