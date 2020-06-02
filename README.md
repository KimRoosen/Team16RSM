=========================================================
  D A T A S E T / D A T A B A S E  D E S C R I P T I O N
==========================================================

(template based on https://arxiv.org/abs/1803.09010)


* Name of the dataset/database:
Predicting quarantine behaviours:
Examining the reaction of Dutch citizens through data collection on Twitter
during a live COVID-19 press conference

==========================================================
1. MOTIVATION
==========================================================

1.1  For what purpose was the dataset created?
     Was there a specific task in mind? Was there
         a specific gap that needed to be filled?
     Please provide a description.

The purpose of this data collection is to understand how citizens react to
government policies, specifically how Dutch citizens reacted to the extension of
quarantine policies in the Netherlands. By understanding how citizens react,
there is a potential to identify and predict anti-quarantine behaviours such as
the US protests and the 	ability to set contingency plans in place such as
policy adaptations to minimise the spread of COVID-19.

1.2  Who created this dataset
     (e.g., which team, research group) and on behalf of
         which entity (e.g., company, institution, organization)?

The dataset was created by Clarisa van den Heever, Lisa Spaans, Kenneth Boumen
and Kim Roosen who were Research in Social Media students at Tilburg University
at the time of the dataset’s release in 2020.

1.3  Who funded the creation of the dataset?
     If there is an associated grant, please provide
         the name of the grantor and the grant name and number.

NA

1.4  Any other comments?

Data was collected on the 21st of April 2020 by Tilburg University students for
an assignment. The event selected was a live press conference in which
Prime Minister Rutte announced an extension of measures regarding
COVID-19 measures. By collecting data from Twitter during the live press
conference, students were able to attain instant information regarding
citizen reactions to the extended measures. Through data collection students
will not only have the potential to identify possible patterns of
anti-quarantine behaviours but also use the data to answer several
other research questions such as:

1.	Do citizens respond positively to the Dutch government’s policies and
practices regarding COVID-19? In combination with similar datasets, how can
these reactions be compared to other countries? Could the difference be due
to social differences?
2.	Do citizens feel that the government has reacted in a proactive manner
or not? Does the data provide potential reasons why?
3.	Is there a difference in the responses of citizens based on additional
demographic factors?
4.	Does the data provide an indication of a shift in citizen attitude
towards COVID-19 governmental measures over time?
5.    Is there a chance that automated messages/”bot” may have been used
during the collection process? If so, what types of messages/opinions were
they trying to portray?

==========================================================
2. COMPOSITION
==========================================================

2.1  What do the instances that comprise the dataset represent
     (e.g., documents, photos, people, countries)?
     Are there multiple types of instances (e.g., movies,
         users, and ratings; people and interactions between them;
         nodes and edges)?
     Please provide a description.

The instances in the dataset are Tweet Objects. These Tweet Objects comprise of
User objects that indicates the author of the tweet, its unique ID and the
Tweet message (Introduction to Tweet JSON, n.d.). Each message has been tweeted
between 18:45:01 and 19.51:46 (UTC +2) on the 21st of April 2020.

2.2  How many instances are there in total
     (of each type, if appropriate)?

The datasets consists of 12,161 tweets in total of 7,043 unique Twitter users,
of which 4,867 Twitter users tweeted one tweet and 2,176 Twitter users tweeted
two or more tweets.

2.3  Does the dataset contain all possible instances or is it a sample
     (not necessarily random) of instances from a larger set?
     If the dataset is a sample, then what is the larger set?
     Is the sample representative of the larger set
         (e.g., geographic coverage)? If so, please describe how this
         representativeness was validated/verified.
     If it is not representative of the larger set, please describe why not
     (e.g., to cover a more diverse range of instances, because
     instances were withheld or unavailable).

The dataset does not contain all possible instances. It is hard to assess the
representativeness (as well as the quality) of the sample.  The total number of
citizens from which the sample is drawn is not known, as the number frequently
changes as each citizen chooses to engage in the discussion or not.
This requires server-side access, which we do not have. It is especially
important when wanting to conduct quantitative
analysis (Lomborg & Bechmann, 2014). Tweets were collected during one specific
event related to COVID-19. Furthermore it is difficult to fully determine
relationships other than the relationships between users through the
Retweet and Quote Tweet functions (Introduction to Tweet JSON, n.d.).

2.4  What data does each instance consist of?
     "Raw" data (e.g., unprocessed text or images)
     or features? In either case, please provide a description.

Each instance contains a tweet (text) with a maximum of 280 characters.
The raw data or Tweet Object (parent object) consists of several  “child
objects/features”. If the tweet is geo-tagged then a location is  given however
most tweets are not geo_enabled. Tweet Objects also include  entities such as
hashtags, user mentions, URLs, locations and language.  Certain instances
include entities such as native media  (photos, videos or animated Gifs). These
Tweet Objects will then  have "extended_entities" with the media_url, the type
of media, size etc.  Certain tweets also include "extended_tweet" which hold
longer  (longer than 140 characters) messages ("full_text"). "extended_tweet"
also  contains "entities" objects including hashtags,  mentions etc
(Introduction to Tweet JSON, n.d.).

Furthermore, the Tweet Objects can include Retweets or Quote Tweets. Retweets
consist of "retweeted_status" objects. The object includes a User object and the
time of the retweet. Quote Tweets include a new Tweet message. Such messages
hold new sets of hashtags, links and in some instances native data such as
pictures, videos and GIFs (Introduction to Tweet JSON, n.d.).

2.5  Is there a label or target associated with each instance?
     If so, please provide a description.

Each Tweet Object (main object/parent object) is associated with multiple labels
(child objects) indicating additional information (e.g. time, text, source and
in replies), user information (e.g. id, name, screen name, location,
description, followers and friends, verification, profile creation etc.) and
entities (e.g. hashtags, URLs, symbols, favorited, retweets and language).
Furthermore, certain objects will have an “extended_tweet” label.

2.6  Is any information missing from individual instances?
     If so, please provide a description, explaining why this information is
     missing (e.g., because it was unavailable). This does not include
    intentionally removed information, but might include, e.g., redacted text.

In some instances the Tweet Object may have missing information (“null”) for
certain entities such as language, timezone, following, geo and location. In
the case of Retweets, ‘geo’ and ‘place’ objects are always null. The reason for
this is that Retweets are used to share tweets of other users with your
followers and no extra content can be shared in the tweet (Introduction to
Tweet JSON, n.d.).

2.7  Are relationships between individual instances made
     explicit (e.g., users' movie ratings, social network links)?
     If so, please describe how these relationships are made explicit.

There are several known relationships between instances. For example, all
individuals who were watching the press conference and wanted to express
opinions and/or concerns about the news via social media. Other relationships
between individual instances include retweets and quote tweets between
individuals. In instances of retweets, individuals simply repost the original
user's text. When a user has retweeted another it will indicate:

     retweeted_status": { "created_at": "Tue Apr 21 17:19:12 +0000 2020", "id":
     1252648088751296512, "id_str": "1252648088751296512", "text": "Goed
     gesproken, @MinPres. Helder en daadkrachtig. Ga nu maar lekker naar huis,
     trek je joggingbroek aan en een bier… https://t.co/dofXlr8X8i", “text": "RT
     @MartijnKonings: Goed gesproken, @MinPres. Helder en daadkrachtig. Ga nu
     maar lekker naar huis, trek je joggingbroek aan en een biertje…".

Quote tweets include new tweet messages added to the retweeted message and
will be displayed as:

     "quoted_status_id": 1252650346482188288, "quoted_status_id_str":
     "1252650346482188288", "quoted_status": { "created_at": "Tue Apr 21
     17:28:10 +0000 2020", "id": 1252650346482188288, "id_str":
     "1252650346482188288", "text": "En dan nu over naar domme vragen van
     journalisten. Begint al goed met die eerste vraag. Manmanman.
     #persconferentie",

2.8  Are there recommended data splits (e.g., training, development/validation,
     testing)?
     If so, please provide a description of these splits, explaining the
     rationale behind them.

It is recommended to use a random split. The data was collected from ten minutes
before the press conference, during the conference and ten minutes afterwards.
Therefore, the tweet content will change throughout this period as users will
discuss different topics (anticipation, measures taken etc). Thus, a random
split is recommended.

2.9  Are there any errors, sources of noise, or redundancies in the dataset?
     If so, please provide a description.

NA

2.10 Is the dataset self-contained, or does it link to or otherwise rely on
     external resources (e.g., websites, tweets, other datasets)?
     If it links to or relies on external resources,
     a) are there guarantees that they will exist, and remain constant,
         over time;
     b) are there official archival versions of the complete dataset
     (i.e., including the external resources as they existed at the
     time the dataset was created);
     c) are there any restrictions (e.g., licenses, fees) associated with
     any of the external resources that might apply to a future user?
     Please provide descriptions of all external resources and any restrictions
     associated with them, as well as links or other access points, as
         appropriate.

The dataset relies on other sources, the instances depend on Twitter and the
tweets of the users. There is no guarantee that these tweets will consist over
time, as Twitter users are able to delete their tweets. However, the data that
has already been collected will remain in the dataset, potential URLs will still
work once a tweet has been deleted (Martineau, 2020).

2.11 Does the dataset contain data that might be considered confidential
     (e.g., data that is protected by legal privilege or by doctor-patient
     confidentiality, data that includes the content of individuals'
     non-public communications)?
     If so, please provide a description.

No. All data was derived from publicly available social media posts and
accounts.

2.12 Does the dataset contain data that, if viewed directly, might be offensive,
     insulting, threatening, or might otherwise cause anxiety?
     If so, please describe why.

Tweets in the dataset express opinions and concerns about publicly made
announcements or public figures. Opinions of people might cause anxiety or be
viewed as offensive or insulting to the people that have been mentioned within
these tweets (e.g. opinions on Prime Minister Rutte).

2.13 Does the dataset relate to people?
     If not, you may skip the remaining questions in this section.

Yes, the dataset contains information on Twitter users that were active during
the press conference. Although it’s assumed that most users are in fact people,
it is important to keep in mind that tweets could potentially be from automated
accounts and not human beings (Wojcik, Messing, Smith, Raine & Hitlin, 2018).
Additional Atom packages can be installed to investigate the probability of a
Twitter user being a “bot” or not.

2.14 Does the dataset identify any subpopulations (e.g., by age, gender)?
     If so, please describe how these subpopulations are identified and
     provide a description of their respective distributions within the dataset.

Of most respondents personal information is known, such as name, language or
location. Subpopulations could be made according to this data. For instance,
subpopulations could be made based on location. However, there are reliability
and validity issues as not all users have enabled certain features such as
geolocation and bias is introduced when trying to make subpopulations.

2.15 Is it possible to identify individuals (i.e., one or more natural persons),
     either directly or indirectly (i.e., in combination with other data)
     from the dataset?
     If so, please describe how.

Each tweet is annotated with the name and id number of the person that sent out
the tweet, including the text of the tweet. Additionally, should the tweet
contain pictures or videos that may include them, it will be easier to identify
who the individual behind the tweet is. It is therefore possible to go to
Twitter and search for the profile of the user and get more information about
who the person really is.

2.16 Does the dataset contain data that might be considered sensitive in
     any way (e.g., data that reveals racial or ethnic origins, sexual
     orientations, religious beliefs, political opinions or union memberships,
     or locations; financial or health data; biometric or genetic data;
     forms of government identification, such as social security numbers;
     criminal history)?
     If so, please provide a description.

The dataset does contain some data that is sensitive, because (political)
opinions are expressed in the tweets. The tweets contain criticism as well as
praise to the COVID-19 policies and the political leaders of The Netherlands.
The dataset is about a national press conference led by Prime Minister Mark
Rutte and therefore this leads to a connection with politics and social issues.
The dataset also contains information on health precautions, locations and
geotracking which could be considered sensitive.

2.17 Any other comments?

It is important to keep in mind that despite data being publicly available,
researchers must practice ethical precautions. Recent events have shown the
consequences of misusing data. Researchers are urged to consider the ethical
implications of their research and take into consideration that despite having
users permission to use the data, these users may not necessarily know the
amount of data that is actually available.

==========================================================
3. COLLECTION PROCESS
==========================================================

3.1  How was the data associated with each instance acquired?
     Was the data directly observable (e.g., raw text, movie ratings),
     reported by subjects (e.g., survey responses), or indirectly
         inferred/derived from other data (e.g., part-of-speech tags, model-based
        guesses for age or language)? If data was reported by subjects or indirectly
     inferred/derived from other data, was the data validated/verified?
     If so, please describe how.

For each tweet that was collected a username was attached to that tweet. With
the username it was possible to get some more information about the user
itself. This can be done by looking at their Twitter account.

3.2  What mechanisms or procedures were used to collect the data
     (e.g., hardware apparatus or sensor, manual human curation,
         software program, software API)?
     How were these mechanisms or procedures validated?

The data is collected by making use of a Twitter API. We first had to make a
developer account to get the credentials. When we had the credentials, we were
able to make use of the API. We set a timeframe to collect the data during the
press conference using a script. After we collected the data, we analysed some
objects with JSON viewer. With this tool the researchers were able to transform
some objects of the raw data in a friendly format that could be analysed. For
validating the data, we inspected the data file to make sure there were no
errors. Beforehand the collecting of data was tested twice and the file was
monitored to see if it kept increasing in size. To prevent crashing of the API,
two members of the team set up the data collection, no error messages were given
during the collection.

3.3  If the dataset is a sample from a larger set, what was the sampling strategy
     (e.g., deterministic, probabilistic with specific sampling probabilities)?

The dataset is a sample of the people that commended on the Dutch press
conference. To capture most of the tweets that relate to this conference we
used hashtags that were the most popular regarding to this event. The hashtags
included: #persconferentie, #coronavirusnl, #coronamaatregelen, #rivm,
#outbreakmanagementteam, #rutte, #dejonge. With this strategy we wanted to
collect most of the tweets related to this press conference.

3.4  Who was involved in the data collection process (e.g., students,
       crowdworkers, contractors) and how were they compensated (e.g., how
         much were crowdworkers paid)?

There were four students involved in the data collection. Two students had the
task to collect the data on their computer. The students did not get paid for
collecting the data.

3.5  Over what timeframe was the data collected? Does this timeframe
     match the creation timeframe of the data associated with the
     instances (e.g., recent crawl of old news articles)?
     If not, please describe the timeframe in which the data associated with the
     instances was created.

The data was collected between 18:45:01 and 19.51:46 (UTC +2) on the 21st of
April 2020. This time slot is based upon the time that the NOS (Dutch news
program) aired the press conference live on Dutch television (18:55 to 19:30
(UTC +2)).

3.6  Were any ethical review processes conducted (e.g., by an institutional
     review board)?
     If so, please provide a description of these review processes, including
     the outcomes, as well as a link or other access point to any
     supporting documentation.

NA

3.7  Does the dataset relate to people?
     If not, you may skip the remainder of the questions in this section.

Yes, each object/tweet gathered is connected to a user of Twitter. This
username is obviously related to a person. Although it’s assumed that most
users are in fact people, it is important to keep in mind that tweets could
potentially be from automated accounts and not human beings (Wojcik et al.,
2018). Additional Atom packages can be installed to investigate the probability
of a Twitter user being a “bot” or not.

3.8  Did you collect the data from the individuals in question directly,
     or obtain it via third parties or other sources (e.g., websites)?

The data was collected from a public social media platform, Twitter

3.9  Were the individuals in question notified about the data collection?
     If so, please describe(or show with screenshots or other information) how
     notice was provided, and provide a link or other access point to,
     or otherwise reproduce, the exact language of the notification itself.

No, the individuals do not know that their data is used for research. Either
when subscribing to a public social media platform most of the users know in
general that their data could be used for research. Either there are some
limitations for the researches when collecting the data. This because a Twitter
API is used and there are some legal conditions when making use of this
application. Some important legal conditions: - Twitter will have the rights on
the data and you cannot sell the data to third parties -   If your service adds
location information you have to disclose this to the users

3.10 Did the individuals in question consent to the collection and use of their
     data?

If so, please describe (or show with screenshots or other information) how
consent was requested and provided, and provide a link or other access point to,
or otherwise reproduce, the exact language to which the individuals consented.

3.11 If consent was obtained, were the consenting individuals provided with a
     mechanism to revoke their consent in the future or for certain uses?
     If so, please provide a description, as well as a link or other access
     point to the mechanism (if appropriate).

Not specifically, but when you subscribe to a platform as Twitter you have to
accept the terms and conditions. With agreeing on these terms, you also agree
on that your data could be used for purposes such as research. However, users
may not be aware of the amount of data that can be collected by researchers.

3.12 Has an analysis of the potential impact of the dataset and its use on data
     subjects (e.g., a data protection impact analysis)been conducted?
     If so, please provide a description of this analysis, including the
         outcomes, as well as a link or other access point to any supporting
         documentation.

No, the data was gathered from a public source, there was no explicit
informing that their tweets were used for research.

3.13 Any other comments?

NA

==========================================================
4. PREPROCESSING/CLEANING/LABELING
==========================================================

4.1  Was any preprocessing/cleaning/labeling of the data done (e.g.,
       discretization or bucketing, tokenization, part-of-speech tagging,
         SIFT feature extraction, removal of instances, processing of
         missing values)? If so, please provide a description. If not, you may skip
         the remainder of the questions in this section.

4.2  Was the "raw" data saved in addition to the
     preprocessed/cleaned/labeled data (e.g., to support unanticipated
         future uses)? If so, please provide a link or other access point to
         the "raw" data.

4.3  Is the software used to preprocess/clean/label the instances available?
     If so, please provide a link or other access point.

4.4  Any other comments?


==========================================================
5. USES
==========================================================

5.1  Has the dataset been used for any tasks already?
     If so, please provide a description.

NA

5.2  Is there a repository that links to any or all papers or systems
     that use the dataset?
     If so, please provide a link or other access point.

NA

5.3  What (other) tasks could the dataset be used for?

The information in the dataset could be used to gather more information about
active twitter users during political events. Data can also be used in addition
to other data to answer the potential research questions stated in the
motivation. For example, if there is a difference in responses based on
additional demographic data or how these responses can be compared to those in
other countries.

5.4  Is there anything about the composition of the dataset or the way it was
         collected and preprocessed/cleaned/labeled that might impact future uses?
         For example, is there anything that a future user might need to know to
         avoid uses that could result in unfair treatment of individuals or groups
         (e.g., stereotyping, quality of service issues) or other undesirable harms
         (e.g., financial harms, legal risks) If so, please provide a description.
         Is there anything a future user could do to mitigate these undesirable
         harms?

There is minimal risk for harm: the data was already public. However, it should
be kept in mind that the data includes sensitive information such as political
views, strong language and subjective opinions. As such, future researchers need
to be aware that the data includes subjectivity and should not be misused by
stereotyping of groups or making use of only certain data in order to support a
theory etc.

5.5  Are there tasks for which the dataset should not be used?
     If so, please provide a description.

The dataset should not be used for unethical practices. Despite having users
permission to use the data, these users may not necessarily know the amount of
data that is actually available. Furthermore, data should not be used for
purposes other than academic research practices, for example making use of the
data for political marketing purposes.

5.6  Any other comments?

Future researchers must take into account the societal contexts in which we are
living when making use of this data. Researchers must accept responsibility for
their use of the data. As well as ensure that an objective and analytical focus
is kept when manipulating the data rather than manipulating data to fit a
particular agenda or research question.

==========================================================
6. DISTRIBUTION
==========================================================

6.1  Will the dataset be distributed to third parties outside of the entity
     (e.g., company, institution, organization) on behalf of which the
     dataset was created?
     If so, please provide a description.

6.2  How will the dataset will be distributed(e.g.,tarball on website, API,
       GitHub)? Does the dataset have a digital object identifier (DOI)?

6.3  When will the dataset be distributed?

6.4  Will the dataset be distributed under a copyright or other intellectual
     property(IP) license, and/or under applicable terms of use (ToU)?
     If so, please describe this license and/or ToU, and provide a link or other
     access point to, or otherwise reproduce, any relevant licensing terms or
         ToU (Terms of Use), as well as any fees associated with these restrictions.

6.5  Have any third parties imposed IP-based or other restrictions on the
     data associated with the instances?
     If so, please describe these restrictions, and provide a link or other
     access point to, or otherwise reproduce, any relevant licensing terms,
     as well as any fees associated with these restrictions.

6.6  Do any export controls or other regulatory restrictions apply to the
     dataset or to individual instances?
     If so, please describe these restrictions, and provide a link or other
     access point to, or otherwise reproduce, any supporting documentation.

6.7  Any other comments?

==========================================================
7. MAINTENANCE
==========================================================

7.1  Who is supporting/hosting/maintaining the dataset?

7.2  How can the owner/curator/manager of the dataset be contacted
     (e.g., email address)?

7.3  Is there an erratum?
     If so, please provide a link or other access point.

7.4  Will the dataset be updated (e.g., to correct labeling errors, add
     new instances, delete instances)?
     If so, please describe how often, by whom, and how updates will
     be communicated to users (e.g., mailing list, GitHub)?

7.5  If the dataset relates to people, are there applicable limits on the
     retention of the data associated with the instances
     (e.g., were individuals in question told that their data would be retained
       for a fixed period of time and then deleted)?
     If so, please describe these limits and explain how they will be enforced.

7.6  Will older versions of the dataset continue to be
     supported/hosted/maintained?
     If so, please describe how. If not, please describe how its obsolescence
     will be communicated to users.

7.7  If others want to extend/augment/build on/contribute to the dataset,
     is there a mechanism for them to do so?
     If so, please provide a description. Will these contributions be
     validated/verified?
     If so, please describe how. If not, why not? Is there a process for
     communicating/distributing these contributions to other users?
     If so, please provide a description.

7.8  Any other comments?


8. RESOURCES
==========================================================

Introduction to Tweet JSON. Retrieved 26 April 2020, from
https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/
intro-to-tweet-json#fundamentals

Lomborg, S., & Bechmann, A. (2014). Using APIs for Data Collection on Social
Media. The Information Society, 30(4), 256–265.
https://doi.org/10.1080/01972243.2014.915276 Martineau, P. (2020).

Tweets Can Be Deleted, but Your Likes Are Forever. Retrieved 30 April 2020, from
https://www.wired.com/story/tweets-ephemeral-likes-forever/

Wojcik, S., Messing, S., Smith, A., Raine, L., & Hitlin, P. (2018).
Twitter Bots: An Analysis of the Links Automated Accounts Share.
Retrieved 30 April 2020, from
https://www.pewresearch.org/internet/2018/04/09/bots-in-the-twittersphere/
