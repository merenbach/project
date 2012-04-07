#import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'merenbachdotcom.settings'
#export DJANGO_SETTINGS_MODULE = merenbachdotcom.settings
import os
os.environ['OVERLOAD_SITE'] = 'merenbach'
#alias mga="/usr/bin/env OVERLOAD_SITE=merenbach python manage.py"
from django.core.management import setup_environ
from project import settings
setup_environ(settings)
from project.websites.merenbach.software.models import Software
import datetime
from django.utils.timezone import utc
gettext = lambda s: s


TITLES = (
        {
            'title': 'ChemBuddy',
            'slug': 'chembuddy',
            'version': '1.1a7',
            'summary': 'Legacy, open-source chemical analysis program for students, chemists, and hobbyists alike; supplanted by Valence',
            'tags': 'legacy, application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 55),
            'description': gettext("""
***Note: ChemBuddy is returning as a new program under a new name, Valence, with a new interface, improved robustness, and many bug-fixes.***

ChemBuddy is an open-source chemical analysis program for students, chemists, and hobbyists alike. It performs many functions from various aspects of chemistry. It has gone in and out of development through the years, and a European firm is currently sharing the name for one of their chemical analysis products (mine is not to be confused with theirs, which I'm certain is far better&mdash;although not, last I checked, for Mac). Features include:

* **Conversions**: Heat, Mass, Moles, Pressure, Temperature, and Volume
* **Gases**: Boyle's Law, Charles' Law, Combined Gas Law, Gay-Lussac's Law, and Ideal Gas Law
* **Solutions**: Concentration, Dilution, Molality, Molarity, Normality, Solubility, and Titration
* **Miscellaneous**: Stoichiometry
* A very pretty, if somewhat incomplete in its implementation, **periodic table of the elements**, with a basic table, a crystal-structures table, an electron-blocks table, a radioactivity table, and a basic states-of-matter table.
* More features are planned for future releases!

[Click here](http://sourceforge.net/projects/chembuddy) to visit the ChemBuddy project page on SourceForge.
            """),
            },
        {

            'title': 'DiceX',
            'slug': 'dicex',
            'version': '1.4.0',
            'summary': 'Legacy dice-roller for Mac OS X. Superseded by Polymatic',
            'tags': 'legacy, application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 54),
            'description': gettext("""
***Note: DiceX has been rewritten as a new program under a new name, Polymatic, with a better interface, better error-checking, and many, many bug-fixes.***

DiceX was a dice-roller for Mac OS X, written in Cocoa.  It is now legacy, but its source (largely useless, I might add, considering that the successor to DiceX, Polymatic, is now open-source) is still available on SourceForge.

[Click here](http://sourceforge.net/projects/dicex) to visit the DiceX project page on SourceForge.
            """),
            },
        {
            'title': 'Divisilist',
            'slug': 'divisilist',
            'version': '1.2',
            'summary': 'Manipulates textual lists for the user to partition, sort, shuffle, manually rearrange, import, and export',
            'tags': 'application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 35),
            'description': gettext("""
Divisilist manipulates lists for the user to partition, sort, shuffle, manually rearrange, import, and export.  Divisilist also has a full-screen kiosk display for the presentation of basic lists.

The program began its life, years ago, as NamePicker, which took (in one incarnaton) a list of entries in a table and drew at random from among them, displaying the results separated by commas in a text box.  It has evolved greatly since then, as I hope will be apparent to those who try the new version; instead of using a text box, it employs an outline view, and it has many more bells and whistles than a simple list-keeper.

**What's new in 1.2?**  (The below list includes the entire course of alpha development.)

* Fixed a bug that made it impossible to turn off randomization for the lottery mode.
* Fixed a bug that caused removal of blank entries to remove all the non-blank entries instead.
* Improved sorting of entries and records such that lists are now case-insensitive and order numeric strings properly.
* Implemented rudimentary AppleScript support for setting and retrieving.
* Addressed an issue where type-select in the entries, results, and kiosk records table and outline views would cause a system beep.
* Addressed a display issue in the title of the online help.
* Addressed an issue wherein too small a text size in the kiosk would cause the text to become truncated vertically.
* Addressed an issue wherein high numbers entered into the count parameter fields might prevent the shuffle mode from working properly.
* Addressed an issue wherein setting an empty value for the list count would cause an error.
* Fixed a bug in the copying code that prevented undo from working properly.
* Refined copy-paste code.
* Updated group-generation code.
* Placed hard range limits, between zero and a million, inclusive, on the range sheet.
* Expanded undo and redo code to apply to flagged/included checkboxes and, perhaps just as importantly, result partitioning.
* Added a feature to remove blank entries.
* Implemented themeable reports (currently with a second report theme, "Camouflage").
* Added auto-expand functionality to preferences.
* Moved auto-scroll functionality  to preferences (from main window).
* Fixed some code glitches in the online help.
* Made partitioning code more responsive to user cancellation.
* Many other internal changes.
* Implemented undo support.
* Implemented a lottery partition mode.
* Changed entry sorting menu to an Entries List menu with an option to replace entries with, in addition to the existing sorting options, an item to replace the entries with numbers within a specified range.
* Added a "repeat entries" option.
* Added a "randomize entries" option.
* Split the partition count box into List Count, Group Count, and Group Size boxes, combinations of each of which apply to different partition modes.
* The locations of the kiosk button and the start/stop partitioning buttons have been swapped in the toolbar.
* Several alerts have been rewritten and recoded for both clarity and ease of localization.
* Updated the online help significantly.
* Improved (hopefully) drag-and-drop code.
* Updated menu bar items for kiosk.
* Fixed split view resizing behavior.
* Rearranged the interface some more.
* Divided preference for auto-editing (upon record/entry insertion) into two preferences, one for main-window entries, the other for kiosk records.
* Once again, a thoroughly redesigned interface. There are nearly far too many changes to count.
* The program is no longer document-based.  It now has a centralized, main window, plus the kiosk.
* The kiosk has been entirely redesigned, with a full-screen display and its own table of entries (which can be imported, exported, and shuffled). 
* Changed shuffling from an entries list feature (which is, actually, still available as a sorting option) to a partitioning feature.
* Many other fixes and improvements.
            """),
            },
        {
            'title': 'Frotz',
            'slug': 'frotz',
            'version': '2.43 (r1)',
            'summary': 'A port of the command-line tool Frotz, usable for playing text adventures in the Mac OS X Terminal',
            'tags': 'port',
            'pub_date': datetime.datetime(2011, 1, 8, 13, 33),
            'description': gettext("""
This is a Leopard-only version of the command-line tool Frotz, which can be used to play text adventures in the Mac OS X Terminal.  See the installer information screen for further details.

This program is rather out-of-date by now.  Although I have little experience with other interpreters, I recommend the use of programs such as [Zoom](http://www.logicalshift.demon.co.uk/mac/zoom.html) instead.  Many (including Zoom) offer interfaces of their own and do not require the use of the Mac OS X Terminal program, and some are multi-platform.

Needless to say, it costs me nothing to maintain the package in its present state, but I cannot offer much support at this point for this specific archive.  I do not recommend using it, even though it works, unless you have a particular affinity for the Terminal&mdash;or need something quick and simple.
            """),
            },
        {
            'title': 'Geometer',
            'slug': 'geometer',
            'version': '1.4',
            'summary': 'Constructs rasterized representations of polygons of nearly any size, vertex-count, and color',
            'tags': 'legacy, application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 49),
            'description': gettext("""Geometer is a legacy program, last updated in mid-2008 and not currently available, that constructs, and allows for the exportation of, polygons of various sizes, shapes, and colors.  It is currently on hiatus."""),
            },
        {
            'title': 'GlyphHanger',
            'slug': 'glyphhanger',
            'version': '1.0',
            'summary': 'Converts text into images with alpha transparency',
            'tags': 'application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 27),
            'description': gettext("""
GlyphHanger converts text, plain or stylized and input by the user into the main text box, into a TIF-formatted image that it then copies to the pasteboard.  From there, this image can then be pasted into Preview, whence it can be saved to any one of a number of other image formats.  It can also be pasted into a word processing document in Pages, for instance, or into other applications that can read TIF data.

One of GlyphHanger's important features is that images are copied antialiased and with alpha transparency.  This makes it much easier to integrate captured text into a logo than it would be with a screenshot.  No lasso tool required!
            """),
            },
        {
            'title': 'LifeLines',
            'slug': 'lifelines',
            'version': '3.0.46.1 (r2)',
            'summary': 'A command-line tool to manipulate family tree data in GEDCOM format',
            'tags': 'port',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 04),
            'description': gettext("""
From the [LifeLines](http://lifelines.sourceforge.net/) user manual:

> LifeLines is a genealogy program that runs on UNIX systems. It maintains
> genealogical records (persons, families, sources, events and others) in a
> database, and generates reports from those records. There are no practical
> limits on the number of records that can be stored in a LifeLines database,
> nor on the amounts or kinds of data that can be kept in the records. LifeLines
> does not contain built-in reports. Instead it provides a programming subsystem
> that you use to program your own reports and charts. The programming subsystem
> also lets you query your databases and process your data in any way. LifeLines
> uses the terminal independent features of UNIX to provide a screen and menu
> based user interface.

Please note that I am not the author, but instead have made a simple port to Mac OS X of existing software.
            """),
            },
        {
            'title': 'Polymatic',
            'slug': 'polymatic',
            'version': '1.1',
            'summary': 'Flexible dice-roller',
            'tags': 'application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 28),
            'description': gettext("""
Polymatic, formerly known as DiceX, embodies a complete rewrite of its predecessor.  The die-rolling algorithms are more robust; the interface is cleaner and less cluttered; and your options have expanded!  Although the detailed hierarchical concept of groups comprising pools, and pools comprising dice, is not necessarily unique, I have yet to see it executed this way in a comparable program, and with the slight expense of a little complexity, it affords great flexibility.

There are two windows in Polymatic, the main window and the log.  The main window houses the basic configuration options, as well as a basic results table and a tab view with all sorts of juicy options that you can configure.  Want to add a per-die bonus of 7 and a per-pool multiplier of 2?  You got it.  Want to drop the three lowest dice and the one highest die?  No problem.  Want to reroll any dice or pools that are under and/or over specified values?  Polymatic can do that, too.

The log shows a complete breakdown of the groups, pools, and dice, each in a separate table.  Every time that you roll the dice, another row will be added to the groups table; when activated, that item will show a breakdown of its pools in the Pool table (no joke intended); and clicking on a pool will show a breakdown of its dice in the Die table.  It takes a small amount of getting used to, but is meant to display as complete a breakdown as possible.
            """),
            },
        {
            'title': 'Quotient',
            'slug': 'quotient',
            'version': '1.5.3',
            'summary': 'Calculates rational quotients out to any level of precision, then (optionally) detects any repeating portion of the decimal',
            'tags': 'application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 30),
            'description': gettext("""
A quotient may extend off the screen of your calculator, such as when you divide 1 by 7.  It turns out, however, that at least some part of what follows the decimal point repeats indefinitely.

This is what I grew up calling a repeating decimal&mdash;that is to say, a portion of the decimal repeats itself infinitely as a *repetend*.  As an example, the fraction <sup>1</sup>/<sub>7</sub> equals 0.142857142857142857142&hellip;&hellip;  In this case, **142857**, or any wrapped variant (such as 428571 or 857142), would be the repetend due to its being the smallest repeating chunk.

Quotient enters the scene here.  The program writes the quotient of any integer division&mdash;to a user-specified level of decimal precision&mdash;into a text box, whence it can be copied to the Clipboard, or exported (along with the rest of the calculation parameters) to a text file.

A repetend locator rounds out the program's functionality, employing an algorithm with the ability to determine a repeating end-segment portion in any finite-length string, which the result text box then displays.  The only known issue with this feature is that, while determining the repetend of a short quotient string remains fairly fast, it can take a long time to determine that of a longer one.  Furthermore, some short strings are slow while other longer ones go quickly.  This issue is difficult to avoid, since the algorithm divides the entire string into pieces repeatedly and must process them again each time through.

What's New in Quotient 1.5.3?

* Fixed a bug that prevented the online help from loading.
* Made the main window resizable once more.
* Increased the height of the main window.
* Added an adjustable slider between the quotient and repetend text views.
* Rearranged the main window slightly.
            """),
            },
        {
            'title': 'Randomness',
            'slug': 'randomness',
            'version': '1.5.5b1',
            'summary': 'Legacy, multifunction random-number generator',
            'tags': 'legacy, application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 45),
            'description': gettext("""
*** Please note that Randomness is now a legacy application and is no longer under active development.  Its functions are now largely a part of Divisilist, save for random string generation (which unfortunately has no current equivalent).  For lottery, list, or random number drawings, I urge users to make the switch to Divisilist.***

Randomness is a multifunction random number generator, comprising a simple number generator, a numeric-string generator, a lottery-number picker, and a list drawing interface.

What's new?

* Implemented a "List" drawing interface.
* It is now possible to stop a generation before it has completed.
* Updated the user interface significantly.
* Improved much of the internal program design.
* The program is now (hopefully) thread-safe.
            """),
            },
        {
            'title': 'TiMidity++',
            'slug': 'timidity',
            'version': '2.13.2 (r2)',
            'summary': 'A command-line software synthesizer. Can be used to convert MOD music files into WAV audio files',
            'tags': 'port',
            'pub_date': datetime.datetime(2011, 1, 8, 13, 53),
            'description': gettext("""
From the [TiMidity++ home page](http://timidity.sourceforge.net/) on SourceForge:

> TiMidity++ is a software synthesizer. It can play MIDI files by converting
> them into PCM waveform data; give it a MIDI data along with digital instrument
> data files, then it synthesizes them in real-time, and plays. It can not only
> play sounds, but also can save the generated waveforms into hard disks as
> various audio file formats.

One good use for TiMidity is to convert MOD music files (remember those?) into AIFF files, which can then be converted into AAC or MP3 tracks from within iTunes.  **An uninstallation script is provided and is installed into `/usr/share/timidity/uninstall-timidity.sh`**.

This software is released under the GNU General Public License (version 2), and I have bundled it into a Mac OS X installer package. Please note that **I am not the author**, and thus cannot provide much more than rudimentary technical support, except in the matters of installation&mdash;but please feel free to contact me with any problems that you might have.
            """),
            },
        {
            'title': 'Transcoder',
            'slug': 'transcoder',
            'version': '1.0',
            'summary': 'Experimental program to convert text between typesets, such as UTF-8',
            'tags': 'application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 37),
            'description': gettext("""
If you have an iTunes track with garbled IDE tags or a translated document with gibberish for text, Transcoder may be able to help.  Copy the text in question into the data into the top text area, then select the source encoding (generally Western of some sort, either Mac Roman or ISO Latin 1) and target encoding (say, a Japanese encoding of some sort)&mdash;and, optionally, a median encoding to go "chain" between the two&mdash;and click the Transcode button in the toolbar.  Presto!  The original glyphs appear in the lower text box in their original beauty.

For an example of how the process works: Take the text **&#241;&#211;&#236;&#225;&#238;&#184;&#243;e&#233;&#8747;** and select "Western (Mac OS Roman)" as the source encoding and "Japanese (Mac OS)" as the target encoding.  Click the Transcode Text button and you'll see **&#30690;&#23798;&#32654;&#23481;&#23460;** (Yazima Beauty Salon, a Japanese musical group) appear in the target text box.**

With some fiddling, however, Transcoder can identify a wide variety of garbled IDE tags and other textual corruption.  Unfortunately, this process may require that you open the MP3 in a text editor to extract tags uninterpreted by the iTunes text engine, and as such the program can sometimes require some tinkering with the encoding settings.  In order to get results through pasting the garbled tags directly from iTunes itself, one may even have to go through a string of conversions.  I am considering trying to figure out a way to automate the process.
            """),
            },
        {
            'title': 'Valence',
            'slug': 'valence',
            'version': '1.0a2',
            'summary': 'Chemical-analysis application for conversions and calculations. Successor to ChemBuddy',
            'tags': 'application',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 20),
            'description': gettext("""
In the footsteps of ChemBuddy 1.1a7 and 1.1a8 comes a new program, Valence, with a new name and a new interface, and many improvements!  This is the second alpha, and there are still probably a few bugs in the code.  As this is a prerelease, the interface is neither yet finalized, finished, nor polished.  *Please don't use it for production work at this time!*

Valence is a chemical analysis assistant for students, chemists, and hobbyists alike. It performs calculations involved in various aspects of chemistry. Features include:

* **Conversions**: Heat, Mass, Moles, Pressure, Temperature, and Volume
* **Gases**: Boyle's Law, Charles' Law, Combined Gas Law, Gay-Lussac's Law, and Ideal Gas Law
* **Solutions**: Concentration, Dilution, Molality, Molarity, Normality, Solubility, and Titration
* **Miscellaneous**: Equilibrium
* **Stoichiometry**: Heat Energy Transferred, Limiting Reagents
* A **periodic table of the elements**, with a basic table, a crystal-structures table, an electron-blocks table, a radioactivity table, and a basic states-of-matter table.
* An in-progress **molar mass calculator**.
* More features planned.
            """),
            },
        {
            'title': 'Wget',
            'slug': 'wget',
            'version': '1.12 (r2)',
            'summary': 'Automated Web-download tool for the command-line',
            'tags': 'port',
            'pub_date': datetime.datetime(2011, 1, 8, 14, 00),
            'description': gettext("""
From the Free Software Foundation's [Wget home page](http://www.gnu.org/software/wget/):

> GNU Wget is a free software package for retrieving files using HTTP, HTTPS and
> FTP, the most widely-used Internet protocols. It is a non-interactive
> commandline tool, so it may easily be called from scripts, cron jobs,
> terminals without X-Windows support, etc.  GNU Wget has many features to make
> retrieving large files or mirroring entire web or FTP sites easy&hellip;

This software is released under the GNU General Public License (version 3), and I have bundled it into a Mac OS X installer package.  I am not the author, and thus cannot provide detailed technical support on the intricacies of program operation, except perhaps in the matters of installation&mdash;but please feel free to contact me with any problems that you might have.
            """),
            }
        )

software_titles = Software.objects.all()
software_titles.delete()

for a in TITLES:
    s = Software(
            title=a['title'],
            version=a['version'],
            slug=a['slug'],
            summary=a['summary'],
            #is_published=a['is_publish'],
            is_published=True,
            tags=a['tags'],
            description=a['description'],
            pub_date=a['pub_date'].replace(tzinfo=utc),
            #pub_date = datetime.datetime.now(),
            )
    s.save()
