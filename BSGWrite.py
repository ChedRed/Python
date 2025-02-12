fp = open('/Users/ryanchou/Library/Application Support/Steam/steamapps/common/Besiege/Besiege.app/Contents/SavedMachines/Allblocks.bsg', 'w')
fp.write('<?xml version="1.0" encoding="utf-8"?>')
fp.write('\n' + '<!--Besiege machine save file.-->')
fp.write('\n' + '<Machine version="1" bsgVersion="1.3" name="AllBlocks">')
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
i = -1
for x in range(35):
    for y in range(3):
        for z in range(5):
            i+= 1
            j = str(i)[-1:]
            if (i < 10):fp.write('\n' + '        <Block id="' + str(i) + '" guid="00000000-0000-0000-0000-00000000000' + str(i) + '">')
            elif (i < 100):fp.write('\n' + '        <Block id="' + str(i) + '" guid="00000000-0000-0000-0000-0000000000' + str(i) + '">')
            elif (i < 1000):fp.write('\n' + '        <Block id="' + str(i) + '" guid="00000000-0000-0000-0000-000000000' + str(i) + '">')
            elif (i < 10000):fp.write('\n' + '        <Block id="' + str(i) + '" guid="00000000-0000-0000-0000-00000000' + str(i) + '">')
            else:fp.write('\n' + '        <Block id="' + str(i) + '" guid="00000000-0000-0000-0000-0000000' + str(i) + '">')
            fp.write('\n' + '            <Transform>')
            fp.write('\n' + '                <Position x="' + str(x * 3 - 7.5) + '" y="' + str((y * 3.3 + 1)) + '" z="' + str(z * 2.5 - 8.5) + '" />')
            fp.write('\n' + '                <Rotation x="0" y="0" z="0" w="1" />')
            fp.write('\n' + '                <Scale x="1" y="1" z="1" />')
            fp.write('\n' + '            </Transform>')
            fp.write('\n' + '            <Data />')
            fp.write('\n' + '        </Block>')
fp.write('\n' + '    </Blocks>')
fp.write('\n' + '</Machine>')
fp.close()