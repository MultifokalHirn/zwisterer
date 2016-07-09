alive_color = 7
width = 128
height = 128
board_i = 1
boards = {{}, {}}

function get(bi,x,y)
 if((x<1)or(x>width)or(y<1)or(y>height))then
  return 0
 end
 return boards[bi][y][x]
end

for y=1,height do
 boards[1][y] = {}
 boards[2][y] = {}
 for x=1,width do
  boards[1][y][x] = 0
  boards[2][y][x] = 0
 end
end

-- draw a pentomino
boards[1][60][64] = 1
boards[1][60][65] = 1
boards[1][61][63] = 1
boards[1][61][64] = 1
boards[1][62][64] = 1
boards[1][60][63] = 1
boards[1][60][66] = 1
boards[1][61][63] = 1
boards[1][61][66] = 1
boards[1][62][62] = 1

cls()
while true do
 for y=1,height do
  for x=1,width do
   pset(x-1,y-1,boards[board_i][y][x] * alive_color)
  end
 end
 flip()
 other_i = (board_i % 2) + 1
 for y=1,height do
  for x=1,width do
   neighbors = (
    get(board_i,x-1,y-1) +
    get(board_i,x,y-1) +
    get(board_i,x+1,y-1) +
    get(board_i,x-1,y) +
    get(board_i,x+1,y) +
    get(board_i,x-1,y+1) +
    get(board_i,x,y+1) +
    get(board_i,x+1,y+1))
   if ((neighbors == 3) or
       ((boards[board_i][y][x] == 1) and
        neighbors == 2)) then
    boards[other_i][y][x] = 1
   else
    boards[other_i][y][x] = 0
   end
  end
  board_i = other_i
 end
end
