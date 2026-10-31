UNREACHABLE['Atom.<init>'] = ('no_trigger_in_app',
    'The constructor runs only when Pow builds an Atom (new Atom at Pow.java:44, 60, 84). Pow is built only by Factor.java:77, inside the parser. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:27-53; com/wildplot/android/parsing/Pow.java:44, 60, 84; com/wildplot/android/parsing/Factor.java:77; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.getAtomType'] = ('no_trigger_in_app',
    'Getter. Callers are Pow.java:45, 61, 85 (atom.getAtomType()), inside the Pow chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:149-151; com/wildplot/android/parsing/Pow.java:45, 61, 85; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.getValue'] = ('no_trigger_in_app',
    'Callers are Pow.java:105, 107, 109 (atom.getValue()), inside the Pow chain. Its body dispatches to atomObject at Atom.java:162. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:153-167; com/wildplot/android/parsing/Pow.java:105, 107, 109; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsExpInBrackets'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:35), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:35, 56-69; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsFunctionMath'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:37), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:37, 71-81; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsFunctionX'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:39), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:39, 83-93; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsFunctionXY'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:41), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:41, 95-105; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsNumber'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:43), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:43, 107-116; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsXVariable'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:45), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:45, 118-126; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsYVariable'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:47), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:47, 128-136; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.initAsVariable'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor Atom.<init> (Atom.java:49), so it is unreachable with it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:49, 138-147; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom.isVariable'] = ('no_trigger_in_app',
    'Callers are Pow.java:120, 123 (atom.isVariable()), inside the Pow chain. Its body dispatches to atomObject at Atom.java:179. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:169-184; com/wildplot/android/parsing/Pow.java:120, 123; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['Atom$AtomType.<clinit>'] = ('no_trigger_in_app',
    'The enum initializer runs on the first use of Atom.AtomType. Every use is inside com/wildplot/android/parsing (Atom.java:22-23, 31, 51, 63; NumberAtom.java:27; VariableAtom.java:28; FunctionXAtom.java:23; FunctionXYAtom.java:31), and none is outside the package. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/Atom.java:22-23, 31, 51, 63; com/wildplot/android/parsing/AtomTypes/NumberAtom.java:27; com/wildplot/android/parsing/AtomTypes/VariableAtom.java:28; com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:23; com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:31; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new FunctionXAtom in Atom.java:84 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:28-35; com/wildplot/android/parsing/Atom.java:84; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. The only caller is Atom.java:85 (functionXAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:85-87; com/wildplot/android/parsing/Atom.java:85; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). The method has no other caller. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:64-72; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.init'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor FunctionXAtom.<init> (FunctionXAtom.java:31). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:31, 37-62; com/wildplot/android/parsing/Atom.java:84; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXAtom.java:74-83; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new FunctionXYAtom in Atom.java:96 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:37-44; com/wildplot/android/parsing/Atom.java:96; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. The only caller is Atom.java:97 (functionXYAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:27-29; com/wildplot/android/parsing/Atom.java:97; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:84-92; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.init'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor FunctionXYAtom.<init> (FunctionXYAtom.java:40). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:40, 46-82; com/wildplot/android/parsing/Atom.java:96; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['FunctionXYAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/FunctionXYAtom.java:94-102; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new MathFunctionAtom in Atom.java:72 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:32-42; com/wildplot/android/parsing/Atom.java:72; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.getMathType'] = ('no_trigger_in_app',
    'Getter. The only caller is Atom.java:73 (mathFunctionAtom.getMathType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:138-140; com/wildplot/android/parsing/Atom.java:73; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). Its one other call is the constructor self-call at MathFunctionAtom.java:39. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:39, 95-126; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.init'] = ('no_trigger_in_app',
    'Private. The only caller is the constructor MathFunctionAtom.<init> (MathFunctionAtom.java:34). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:34, 46-92; com/wildplot/android/parsing/Atom.java:72; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain), and the constructor self-call at MathFunctionAtom.java:38. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:38, 128-136; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['MathFunctionAtom$MathType.<clinit>'] = ('no_trigger_in_app',
    'The enum initializer runs on the first use of MathFunctionAtom.MathType: the constructor init (MathFunctionAtom.java:56-76) and Atom.java:73. Every use is inside com/wildplot/android/parsing, and none is outside it. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/MathFunctionAtom.java:26-27, 56-76; com/wildplot/android/parsing/Atom.java:73; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new NumberAtom in Atom.java:108 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:30-37; com/wildplot/android/parsing/Atom.java:108; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. Callers are Atom.java:109 and 111 (numberAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:23-25; com/wildplot/android/parsing/Atom.java:109, 111; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:39-45; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['NumberAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/NumberAtom.java:47-53; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.<init>'] = ('no_trigger_in_app',
    'The only construction is new VariableAtom in Atom.java:139 (Atom.<init> chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:32-40; com/wildplot/android/parsing/Atom.java:139; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.getAtomType'] = ('no_trigger_in_app',
    'Getter. Callers are Atom.java:140 and 142 (variableAtom.getAtomType()), inside the Atom.<init> chain. '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:42-44; com/wildplot/android/parsing/Atom.java:140, 142; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.getValue'] = ('no_trigger_in_app',
    'Reached only as atomObject.getValue() at Atom.java:162 (Atom.getValue, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:46-55; com/wildplot/android/parsing/Atom.java:162; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')

UNREACHABLE['VariableAtom.isVariable'] = ('no_trigger_in_app',
    'Reached only as atomObject.isVariable() at Atom.java:179 (Atom.isVariable, Pow chain). '
    'No app code starts the parser: the only new TopLevelParser is TopLevelParser.java:165 (in createCopy), createCopy() is called only from ReliefDrawer.java:632 and 693, and ReliefDrawer is never constructed (ReliefDrawer.java:120, 145, 165 have no caller).',
    'SRC com/wildplot/android/parsing/AtomTypes/VariableAtom.java:57-60; com/wildplot/android/parsing/Atom.java:179; com/wildplot/android/parsing/TopLevelParser.java:165; com/wildplot/android/rendering/ReliefDrawer.java:632, 693',
    'SOURCE')
