print("What do you want to name your creation?")
input = input("")

fp = open('/Users/ryanchou/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/' + input + '.bsg', 'w')
fp.write('<?xml version="1.0" encoding="utf-8"?>')
fp.write('\n' + '<!--Besiege machine save file.-->')
fp.write('\n' + '<Machine version="1" bsgVersion="1.3" name="' + input + '">')
fp.write('\n' + '    <!--The machine\'s position and rotation.-->')
fp.write('\n' + '    <Global>')
fp.write('\n' + '        <Position x="0" y="1" z="0" />')
fp.write('\n' + '        <Rotation x="0" y="0" z="0" w="1" />')
fp.write('\n' + '    </Global>')
fp.write('\n' + '    <!--The machine\'s additional data or modded data.-->')
fp.write('\n' + '    <Data>')
fp.write('\n' + '        <StringArray key="requiredMods" />')
fp.write('\n' + '    </Data>')
fp.write('\n' + '    <!--The machine\'s blocks.-->')
fp.write('\n' + '    <Blocks>')
i = 0
d = 35
for z in range (8):
    for y in range (8):
        for x in range (8):
            i+= 1
            j = str(i)[-1:]
            if (i < 10):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-00000000000' + str(i) + '">')
            elif (i < 100):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-0000000000' + str(i) + '">')
            elif (i < 1000):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-000000000' + str(i) + '">')
            elif (i < 10000):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-00000000' + str(i) + '">')
            else:fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-0000000' + str(i) + '">')
            fp.write('\n' + '            <Transform>')
            fp.write('\n' + '                <Position x="' + str((x / 2)) + '" y="' + str((y / 2)) + '" z="' + str((z / 2)) + '" />')
            fp.write('\n' + '                <Rotation x="0.7071068" y="5.159959E-07" z="4.290166E-07" w="-0.7071068" />')
            fp.write('\n' + '                <Scale x="1" y="1" z="1" />')
            fp.write('\n' + '            </Transform>')
            fp.write('\n' + '            <Data>')
            fp.write('\n' + '                <Single key="bmt-mass">Infinity</Single>')
            fp.write('\n' + '            </Data>')
            fp.write('\n' + '        </Block>')
d = 57
for z in range (8):
    for y in range (8):
        for x in range (8):
            w = y + 1
            i+= 1
            j = str(i)[-1:]
            if (i < 10):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-00000000000' + str(i) + '">')
            elif (i < 100):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-0000000000' + str(i) + '">')
            elif (i < 1000):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-000000000' + str(i) + '">')
            elif (i < 10000):fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-00000000' + str(i) + '">')
            else:fp.write('\n' + '        <Block id="' + str(d) + '" guid="00000000-0000-0000-0000-0000000' + str(i) + '">')
            fp.write('\n' + '            <Transform>')
            fp.write('\n' + '                <Position x="' + str((x / 2)) + '" y="' + str((w / 2)) + '" z="' + str((z / 2)) + '" />')
            fp.write('\n' + '                <Rotation x="0" y="0" z="0" w="1" />')
            fp.write('\n' + '                <Scale x="1" y="1" z="1" />')
            fp.write('\n' + '            </Transform>')
            fp.write('\n' + '            <Data />')
            fp.write('\n' + '        </Block>')
fp.write('\n' + '    </Blocks>')
fp.write('\n' + '</Machine>')
fp.close()