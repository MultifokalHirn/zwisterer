--pldle
plx=52
ply=122

--ball
ballx=64
bally=64
ballsize=3
ballxdir=5
ballydir=-3

lives=10

function movepl()
 if btn(0) then
  plx-=3
 elseif btn(1) then
  plx+=3
 end
end

function moveball()
 ballx+=ballxdir
 bally+=ballydir
end

function bounceball()

 --left
 if ballx<ballsize then
  ballxdir=-ballxdir
  sfx(0)
 end

 --right
 if ballx>128-ballsize then
  ballxdir=-ballxdir
  sfx(0)
 end

 --top
 if bally<ballsize then
  ballydir=-ballydir
  sfx(0)
 end

 --bottom
 if bally>128-ballsize then
  ballydir=-ballydir
  sfx(0)
 end
end

function hitpl()
 if ballx>=plx and
   ballx<=plx+4 and
   bally>ply then
  sfx(1)
  lives-=1
  ballydir=-ballydir
 end
end

function _update()
 movepl()
 bounceball()
 moveball()
 hitpl()
end

function _draw()

 --clear screen
 rectfill(0,0,128,128,3)

 --draw player
 spr(000,plx,ply)

 --draw ball
 circfill(ballx,bally,ballsize,15)

 --draw score
 print(score,12,6,15)

 --lives
 for i=1,lives do
  spr(001,90+i*8,4)
 end
end
