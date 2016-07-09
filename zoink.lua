f=0 --frame
t=1
c=0
ma=127
function _update()
 f+=t
 --sfx(0)
 if f>ma then
  c+=3
  t=t*(-1)
  sfx(1)
 end

 if f<=0 then
  t=t*(-1)
  sfx(0)
 end
end

function _draw()
 rectfill(0,0,127,127,12)
 i=0
 while(i<20)do
  e=(i*0.5)*t
  e2=10-e

  if btn(0) then
   e+=3
   e2+=3
  end

  if btn(1) then
   e-=3
   e2-=3
  end
  print(f,5,5,4)
  line(0,0,f,127-f,15)
  line(127,127,127-f,f,15)
  i+=1
 end

end
