mtcars[mtcars$cyl<6,] # La como dice que nos muestre en todas las observaciones

orangeec[orangeec$GDP.PC>=1500,]


orangeec[orangeec$Creat.Ind...GDP<=2,]

new_orangeec <- subset(orangeec
)

?orangeec

summary(orangeec)

new_orangeec <- subset(orangeec, Internet.penetration...population > 80 &
                         Education.invest...GDP >=4.5)
new_orangeec

new_orangeec <- subset(orangeec, Internet.penetration...population > 80 &
                         Education.invest...GDP >=4.5, 
                       select = Creat.Ind...GDP)
new_orangeec

rename(orangeec,c('Creat.Ind...GDP' = 'AporteNja'))
