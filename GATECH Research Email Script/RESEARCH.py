import pandas as pd
# from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def main():
    df=pd.read_csv('research.txt', sep=',', header=None, names=['Title', 'Course ID', 'Course #', 'Section', 'Prof Email', 'Prof Name'])

    current_emails = ["sy4@gatech.edu",
"fli@cc.gatech.edu",
"paul.royal@cc.gatech.edu",
"ericson@cc.gatech.edu",
"rf75@mail.gatech.edu",
"mwolf@cc.gatech.edu",
"mstilman@cc.gatech.edu",
"hadi@gatech.edu",
"borodovsky@gatech.edu",
"mcdaniel@cc.gatech.edu",
"asb@cc.gatech.edu",
"oliver.brand@ece.gatech.edu",
"huo@gatech.edu",
"margalit@math.gatech.edu",
"florian.schaefer@cc.gatech.edu",
"xzhang954@gatech.edu",
"turk@cc.gatech.edu",
"arriaga@cc.gatech.edu",
"lukas.graber@ece.gatech.edu",
"etnyre@math.gatech.edu",
"pascal.vanhentenryck@isye.gatech.edu",
"mary.ann.weitnauer@ece.gatech.edu",
"jr25@gatech.edu",
"mengmeng.liu@gatech.edu",
"sman@gatech.edu",
"john.stasko@cc.gatech.edu",
"ml2@gatech.edu",
"sehoonha@gatech.edu",
"xin.chen@isye.gatech.edu",
"echerry30@gatech.edu",
"jichuanyi@gatech.edu",
"pinar@isye.gatech.edu",
"jessica.roberts@cc.gatech.edu",
"nicoleta.serban@isye.gatech.edu",
"sarioglu@gatech.edu",
"kang@math.gatech.edu",
"umit@gatech.edu"]
    
    existing_emails = ["​aluru@cc.gatech.edu",
"​borodovsky@gatech.edu",
"​shb@gatech.edu",
"​polo@gatech.edu",
"​umit@gatech.edu",
"​echerry30@gatech.edu",
"​bdilkina6@gatech.edu",
"​fujimoto@cc.gatech.edu",
"​victorfung@gatech.edu",
"​isbell@cc.gatech.edu",
"​felix.herrmann@gatech.edu",
"​tisaac3@gatech.edu",
"​surya.kalidindi@me.gatech.edu",
"​srijan@gatech.edu",
"​yunan@gatech.edu",
"​badityap@cc.gatech.edu",
"​sherrill@chemistry.gatech.edu",
"​florian.schaefer@cc.gatech.edu",
"​richie@cc.gatech.edu",
"​chaozhang@gatech.edu",
"​xzhang954@gatech.edu",
"​ali.adibi@ece.gatech.edu",
"​mikeb@gatech.edu",
"​bboots@cc.gatech.edu",
"​russ.clark@gatech.edu",
"​munmun.choudhury@cc.gatech.edu",
"​keith@cc.gatech.edu",
"​hadi@gatech.edu",
"​ah260@gatech.edu",
"​hyesoon@cc.gatech.edu",
"​frankli@gatech.edu",
"​orso@cc.gatech.edu",
"​rehg@gatech.edu",
"​riedl@cc.gatech.edu",
"​harish.ravichandar@cc.gatech.edu",
"​thad@gatech.edu",
"​mstilman@cc.gatech.edu",
"​jsun@cc.gatech.edu",
"​vsarkar@gatech.edu",
"​athomaz@cc.gatech.edu",
"​vempala@cc.gatech.edu",
"​wei.xu@cc.gatech.edu",
"​qrzhang@gatech.edu",
"​abowd@gatech.edu",
"​arkin@cc.gatech.edu",
"​arriaga@cc.gatech.edu",
"​manos@gatech.edu",
"​arulraj@gatech.edu",
"​asb@cc.gatech.edu",
"​jdbolter@gatech.edu",
"​michael.borich@gatech.edu",
"​chernova@gatech.edu",
"​maribeth.gandy@imtc.gatech.edu",
"​courtney.crooks@gtri.gatech.edu",
"​frank.dellaert@cc.gatech.edu",
"​bdisalvo@cc.gatech.edu",
"​sauvik@gatech.edu",
"​rad@gatech.edu",
"​irfan@gatech.edu",
"​merrick@cc.gatech.edu",
"​ashok.goel@cc.gatech.edu",
"​daniel.goldman@physics.gatech.edu",
"​gilbert@cc.gatech.edu",
"​matthew.gombolay@cc.gatech.edu",
"​harley.hamilton@cc.gatech.edu",
"​wharris@gatech.edu",
"​keith.mcgreggor@gatech.edu",
"​charlie.kemp@bme.gatech.edu",
"​mkunda@gatech.edu",
"​neha.kumar@gatech.edu",
"​jennifer.kim@cc.gatech.edu",
"​ling.liu@cc.gatech.edu",
"​wenke@cc.gatech.edu",
"​fli@cc.gatech.edu",
"​mynatt@gatech.edu",
"​melodymoorejackson@gatech.edu",
"​cassie.mitchell@bme.gatech.edu",
"​magerko@gatech.edu",
"​cedric.pradalier@gatech.edu",
"​parikh@gatech.edu",
"​thomas.ploetz@gatech.edu",
"​andrea@cc.gatech.edu",
"​rama@gatech.edu",
"​crozell@gatech.edu",
"​jessica.roberts@cc.gatech.edu",
"​krong@gatech.edu",
"​john.stasko@cc.gatech.edu",
"​seth@gatech.edu",
"​turk@cc.gatech.edu",
"​atumanov@gatech.edu",
"​bruce.walker@psych.gatech.edu",
"​wilcox@gatech.edu",
"​dyang888@gatech.edu",
"​tourzhao@gatech.edu",
"​prof@gatech.edu",
"​dbatra@gatech.edu",
"​saadb@chbe.gatech.edu",
"​ericson@cc.gatech.edu",
"​jacobe@gatech.edu",
"​endert@gatech.edu",
"​ada@cc.gatech.edu",
"​hays@gatech.edu",
"​shamkant.navathe@cc.gatech.edu",
"​calton.pu@cc.gatech.edu",
"​moin@gatech.edu",
"​randall@cc.gatech.edu",
"​paul.royal@cc.gatech.edu",
"​jx@cc.gatech.edu",
"​jyoung9@gatech.edu",
"​ewz@cc.gatech.edu",
"​zha@cc.gatech.edu",
"​asensio@pubpolicy.gatech.edu",
"​aianton@gatech.edu",
"​gbrito3@gatech.edu",
"​hic@robotics.gatech.edu",
"​sudheer.chava@scheller.gatech.edu",
"​conte@gatech.edu",
"​xu.chu@cc.gatech.edu",
"​constantine@gatech.edu",
"​cdisalvo@gatech.edu",
"​mdav@gatech.edu",
"​alexandros.daglis@cc.gatech.edu",
"​rf75@mail.gatech.edu",
"​foley@cc.gatech.edu",
"​fortnow@cc.gatech.edu",
"​beki@cc.gatech.edu",
"​ogreen@gatech.edu",
"​seymour.goodman@gatech.edu",
"​sehoonha@gatech.edu",
"​judy@gatech.edu",
"​larryheck@gatech.edu",
"​asaeed@cc.gatech.edu",
"​david.joyner@gatech.edu",
"​taesoo@gatech.edu",
"​karenliu@cc.gatech.edu",
"​drwhite@cc.gatech.edu",
"​fang.liu@gatech.edu",
"​yanni.loukissas@lmc.gatech.edu",
"​mike.mccracken@cc.gatech.edu",
"​leo.mark@pe.gatech.edu",
"​vmuthukumar8@gatech.edu",
"​mcdaniel@cc.gatech.edu",
"​naik@gatech.edu",
"​santosh.pande@cc.gatech.edu",
"​milos@cc.gatech.edu",
"​rpeng@cc.gatech.edu",
"​ashwin.ram@cc.gatech.edu",
"​spencer@cc.gatech.edu",
"​jason.riedy@cc.gatech.edu",
"​mahdir@gatech.edu",
"​alan.ritter@cc.gatech.edu",
"​nicoleta.serban@isye.gatech.edu",
"​lsong@cc.gatech.edu",
"​brendan@ece.gatech.edu",
"​tetali@math.gatech.edu",
"​craig.tovey@isye.gatech.edu",
"​venkat@gatech.edu",
"​rborelav@gatech.edu",
"​mwolf@cc.gatech.edu",
"​maywang@gatech.edu",
"​jeff@imtc.gatech.edu",
"​anqiwu@gatech.edu",
"​sy4@gatech.edu",
"​aaron.young@me.gatech.edu",
"​sean.wilson@gtri.gatech.edu",
"​mustaq@cc.gatech.edu",
"​dhekne@gatech.edu",
"​ledantec@gatech.edu",
"​mengmeng.liu@gatech.edu",
"​yzhang@gatech.edu",
"​durgin@gatech.edu",
"​aholcomb@gatech.edu",
"​omer.inan@ece.gatech.edu",
"​alexandre@gatech.edu",
"​chris.barnes@gatech.edu",
"​pamela.bhatti@ece.gatech.edu",
"​matthieu.bloch@ece.gatech.edu",
"​lukas.graber@ece.gatech.edu",
"​joyelle.harris@ece.gatech.edu",
"​stephen.ralph@ece.gatech.edu",
"​sarioglu@gatech.edu",
"​seun.sangodoyin@gatech.edu",
"​fzhang37@mail.gatech.edu",
"​anderson@gatech.edu",
"​mbakir@ece.gatech.edu",
"​cressler@ece.gatech.edu",
"​stas@gatech.edu",
"​jennifer.hasler@ece.gatech.edu",
"​molzahn@gatech.edu",
"​pvela@gatech.edu",
"​shimeng.yu@ece.gatech.edu",
"​farrokh.ayazi@ece.gatech.edu",
"​oliver.brand@ece.gatech.edu",
"​mark.clements@ece.gatech.edu",
"​mcohen@gatech.edu",
"​mary.ann.weitnauer@ece.gatech.edu",
"​bklein@gatech.edu",
"​aaron.lanterman@ece.gatech.edu",
"​brooks@gatech.edu",
"​em80@gatech.edu",
"​sam.coogan@gatech.edu",
"​magnus.egerstedt@ece.gatech.edu",
"​tushar@ece.gatech.edu",
"​mooney@ece.gatech.edu",
"​arijit.raychowdhury@ece.gatech.edu",
"​sathe@gatech.edu",
"​ye.zhao@me.gatech.edu",
"​paul.voss@ece.gatech.edu",
"​azadeh.ansari@ece.gatech.edu",
"​rbutera@gatech.edu",
"​doug.blough@ece.gatech.edu",
"​abhijit.chatterjee@ece.gatech.edu",
"​vcalhoun@gatech.edu",
"​evadyer@gatech.edu",
"​bill.hunt@ece.gatech.edu",
"​callie.hao@gatech.edu",
"​jichuanyi@gatech.edu",
"​kippelen@gatech.edu",
"​limsk@ece.gatech.edu",
"​glenn.lightsey@gatech.edu",
"​vkm@gatech.edu",
"​bb130@gatech.edu",
"​paul.steffes@ece.gatech.edu",
"​shyh.shen@ece.gatech.edu",
"​bruno.frazier@ece.gatech.edu",
"​bonnie.ferri@gatech.edu",
"​tgaylord@ece.gatech.edu",
"​jskenney@ece.gatech.edu",
"​saibal.mukhopadhyay@ece.gatech.edu",
"​etentze@ece.gatech.edu",
"​mick.west@ece.gatech.edu",
"​alregib@gatech.edu",
"​wcai@gatech.edu",
"​arthur.delarue@isye.gatech.edu",
"​dima.nazzal@gatech.edu",
"​shihao.yang@isye.gatech.edu",
"​cz3@gatech.edu",
"​giangarcia@gatech.edu",
"​pascal.vanhentenryck@isye.gatech.edu",
"​yao.xie@isye.gatech.edu",
"​mathieu.dahan@isye.gatech.edu",
"​deng@gatech.edu",
"​huo@gatech.edu",
"​pinar@isye.gatech.edu",
"​benoit.montreuil@isye.gatech.edu",
"​ashwinpm@gatech.edu",
"​jianjun.shi@isye.gatech.edu",
"​chuck.zhang@gatech.edu",
"​xin.chen@isye.gatech.edu",
"​yuang.chen@gatech.edu",
"​sman@gatech.edu",
"​jsokol@isye.gatech.edu",
"​lxu405@gatech.edu",
"​mbaker@math.gatech.edu",
"​bahtoh@gatech.edu",
"​gg64@gatech.edu",
"​jgonzalez35@gatech.edu",
"​kang@math.gatech.edu",
"​matzi@math.gatech.edu",
"​mbshort@math.gatech.edu",
"​heitsch@math.gatech.edu",
"​lacey@math.gatech.edu",
"​margalit@math.gatech.edu",
"​hmzhou@math.gatech.edu",
"​ib@math.gatech.edu",
"​greg@math.gatech.edu",
"​ablumenthal6@gatech.edu",
"​federico.bonetto@math.gatech.edu",
"​hannahch@gatech.edu",
"​ernest.croot@math.gatech.edu",
"​etnyre@math.gatech.edu",
"​ghomi@math.gatech.edu",
"​harrell@math.gatech.edu",
"​houdre@math.gatech.edu",
"​jyu@math.gatech.edu",
"​rachel@math.gatech.edu",
"​mkuzbary3@gatech.edu",
"​letu@math.gatech.edu",
"​leykin@math.gatech.edu",
"​li@math.gatech.edu",
"​loss@math.gatech.edu",
"​sakis.m@gatech.edu",
"​mtao@gatech.edu",
"​yu@math.gatech.edu",
"​shahaf.nitzan@math.gatech.edu"]
    

    profemail = df.drop_duplicates('Prof Email')


    unqiu_df = pd.unique(df['Prof Name'])

    for i in range(len(existing_emails)):
        existing_emails[i]= existing_emails[i].replace("\u200b", "")
    
    # test = existing_emails.difference(current_emails)

    existing_emails.sort()
    current_emails.sort()
    print(
        set(existing_emails) - set(current_emails))
         

    profemail.to_csv('prof_emails_table.txt', header=None, index=None, sep=',', mode='a')


if __name__ == '__main__':
    main()