# Situation
# In a garden, there are different types of flowers, each type identified by a unique letter.
# The gardener can only fertilize the same type of flowers that are directly next to each other (side-by-side or front-to-back, but not diagonally) in one step.
# The aim is to figure out the smallest number of steps needed to fertilize all the flowers.

visited = set()                             # storing flowers visited by the gardener
garden = ['cmrbfekazymksetvnhaxagucqwbxkslecwcofenjxlgbfqynmvbbmwqpkheiprqmbbsarnqzrusqjlwnzgslfktmkczovidnpmoa', 'mxydbpadkjykrkhdkyahmnpghiugwrzuvigjjlklesfqaqcsnlfvbkifjfniwwbdhxmekhlpqukpajvzflrefmucgptutkodsbmf', 'amqcbujnmwfcpcbgbflasmutixtsznnkrosxqnndbjjzbrxxdkoekpuilosrhysymwluvwdjovsumfgftnvjprrnbxglmkgdlrqg', 'tggfxfmkxkegxscotuiaerwtugdzmzhvyvdqubnxfwfpfmrplnttxmsgntdmdsfxmpufulznhmlebxxfuhjwxcuebsdqnsuuwcky', 'chsmraeosawmxikdpsqzkcayrhnrxwvuibsrpuznsqalrzhfaqdgpbfadjzquswfskryllttnavfcuxbmbkylyfexcmfmfkuzqqa', 'ifmxtcnyeufnlkuglodqjkjqrqpefvrbgiouvcwozyhtbxggtfvsgadkoqwlhsddbltqcmtntapoaxuwxmckigmdfnxaaddlraip', 'unpdtpxdoltnljdzzrclemmcdaedgxqsexqzcxajgdxcioydwwciqeujmovvsdvwjixpitbqyxogtxpfkpbyyrzzjbxptrbyhycr', 'pswribicqkokxmbeujhutwbdkvlwsvosaperzzogsabuabtnzfgvvlppybxdnbvtyqcxoxpdkqnpsnbtzzabneidxzaxllufjksi', 'wbfnbgartxrnusjfdtoyysgxdxtdufuvdpnvqmxyedwqgaqbckhavimykolcmpclargllexzbejdesmrhtzibjzywlwhqtvudzgw', 'xaneylooifingmrfjfpgkvzyelrzdekjkbbytulzrkenzrdabxxsbwodsrntmqacmtmjxxsyfxnnquvupgijemyeaugetnluoboc', 'fxvktjfqogqzssqeuqecdjqxmiiirgnndvkijdlmajztsbyvuvzzeiurwyhgqxrsimnekvapuocbwrctecbbjmnjqgwrijjezqhz', 'jvtsjtgqtsmkkqumouudwmgaihynaxpopvtbmktbohwfkwskzaijewsbxqlqqppcswtdzovrxdtyuuskqwjblailklwxeqgvbgvu', 'dfywnedkabmzuugqrappnyvgpvnbjsfmtornhcftubasqeepjlhhxncvawooanvjrttbimxalfudjylywqnjmjraebqdwyprmlly', 'acimgezpqhvdknecnikrblrgwwvlsznitevbhmkabotihnwpivhpzrefzmviwmcttddmbjkqmkviphsirthnwhsbyrpxggpuknms', 'icheoceijopymbwvqngngugygrcshzrftvmpdvovwfpzllhhczzfdodhprepnxlhajsyhgtfiitfnhedtzphzvwpcakddyipripv', 'cqjhomzaxyekeqtuvijnbumwellzymcctzzlxotxbfdyvemgljipdpujybjwzpxgfkwfegmukmhabmbrfscrswoxouyouwghwbfi', 'pyywqtomwaridmfvvleqtcgqiwdriihudeiwzauyknvdkcpeimkdgeqttmbhfuihvteqsqwsmyilemdqgmaqpqjoulqrksjcvqpr', 'tgqjczqceuicmzgxeqhrpiunvairmhlfvkbepgoawroybnlcbkkgqltqnzshihirrhxzswspvffbkxishruefkbtkacbyhzhtrki', 'goasyzpkkgzytqpnukawevdwuzldijdcocrntpmovhtcxyfxzgbkfjqmkqttubbegwoliztaqivktkzxangyiddgcwjsftbthjcc', 'qxeuemdxhrdnxhfmgnvwewrfolnnxkeruxeohyxjljjadzmotrwfdprftossfiayioodzikbijdvykzryhtjmmgrhnhaphkbhvoz']
steps = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # flowers are considered as neighbours if they are next to each other

def visit_neighbour(i, j):                  # fertilizing all neighbouring flowers of the same type
    for di, dj in steps:
        if ((i+di) > len(garden)-1) or ((i+di) < 0) or ((j+dj) > len(garden[0])-1) or ((j+dj) < 0):     # position is outside of the garden
            continue
        else:
            if (garden[i+di][j+dj] == garden[i][j]) and ((i+di, j+dj) not in visited):                  # neighbouring flowers are of the same type and not yet visited
                visited.add((i+di, j+dj))
                visit_neighbour(i+di, j+dj)
            else:
                continue

def min_steps():                            # find minimum number of steps needed to fertilize all flowers
    count = 0
    for row in range(len(garden)):
        for col in range(len(garden[0])):
            if (row, col) not in visited:
                count += 1
                visited.add((row, col))
                visit_neighbour(row, col)

    print(count)

min_steps()
