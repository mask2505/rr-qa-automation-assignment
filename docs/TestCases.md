# RR QA Automation Assignment - Test Cases

## Test Coverage Summary

| Priority  | Count  |
| --------- | ------ |
| P0        | 22     |
| P1        | 15     |
| P2        | 3      |
| **Total** | **40** |

---

## Priority Definition

| Priority | Description                                                  |
| -------- | ------------------------------------------------------------ |
| P0       | Critical functionality directly impacting core user journeys |
| P1       | Important functionality with moderate business impact        |
| P2       | Low-risk functionality, usability, or visual validation      |

---

## Test Coverage Matrix

| S.No | Test ID | Section               | Summary                                                    | Priority |
| ---- | ------- | --------------------- | ---------------------------------------------------------- | -------- |
| 1    | TC001   | URL                   | Verify Default Landing Page                                | P0       |
| 2    | TC002   | URL                   | Verify Direct Access or Refresh to /popular Route          | P0       |
| 3    | TC003   | Application Header    | Verify App Title is Visible                                | P1       |
| 4    | TC004   | Application Header    | Verify App Title is Clickable and Navigates to Home Page   | P1       |
| 5    | TC005   | Category Filters      | Verify Popular Category Filter                             | P0       |
| 6    | TC006   | Category Filters      | Verify Trending Category Filter                            | P0       |
| 7    | TC007   | Category Filters      | Verify Newest Category Filter                              | P0       |
| 8    | TC008   | Category Filters      | Verify Top Rated Category Filter                           | P0       |
| 9    | TC009   | Discovery Options     | Verify Type Filter Dropdown Shows Movies and TV Shows      | P0       |
| 10   | TC010   | Discovery Options     | Verify Movies Selection in Type Filter                     | P0       |
| 11   | TC011   | Discovery Options     | Verify TV Shows Selection in Type Filter                   | P0       |
| 12   | TC012   | Discovery Options     | Verify Genre Filter Dropdown Shows Available Genres        | P1       |
| 13   | TC013   | Discovery Options     | Verify Genre Filter Functionality                          | P0       |
| 14   | TC014   | Discovery Options     | Verify User Can Select From and To Year                    | P1       |
| 15   | TC015   | Discovery Options     | Verify From Year Cannot Be Greater Than To Year            | P0       |
| 16   | TC016   | Discovery Options     | Verify Rating Filter Functionality                         | P0       |
| 17   | TC017   | Discovery Options     | Verify Multiple Filters Applied Together                   | P0       |
| 18   | TC018   | Search                | Verify Search With Valid Movie Title                       | P0       |
| 19   | TC019   | Search                | Verify Search With Partial Movie Title                     | P1       |
| 20   | TC020   | Search                | Verify Search With Invalid Movie Title                     | P1       |
| 21   | TC021   | Search                | Verify Search Reset Behavior                               | P1       |
| 22   | TC022   | Movie Card Validation | Verify Movie Cards Are Displayed                           | P0       |
| 23   | TC023   | Movie Card Validation | Verify Movie Card Contains Thumbnail                       | P1       |
| 24   | TC024   | Movie Card Validation | Verify Movie Card Contains Title                           | P0       |
| 25   | TC025   | Movie Card Validation | Verify Movie Card Contains Genre                           | P1       |
| 26   | TC026   | Movie Card Validation | Verify Movie Card Contains Release Year                    | P1       |
| 27   | TC027   | Pagination            | Verify Next Page Navigation                                | P0       |
| 28   | TC028   | Pagination            | Verify Previous Page Navigation                            | P1       |
| 29   | TC029   | Pagination            | Verify Page Number Navigation                              | P1       |
| 30   | TC030   | Pagination            | Verify Last Available Page Navigation                      | P0       |
| 31   | TC031   | Pagination            | Verify Pagination Boundary Behavior                        | P1       |
| 32   | TC032   | Scrolling             | Verify Infinite Scroll / Page Scroll Functionality         | P2       |
| 33   | TC033   | Scrolling             | Verify Discovery Filters Remain Accessible During Scroll   | P2       |
| 34   | TC034   | Scrolling             | Verify Pagination Controls Are Reachable Through Scrolling | P1       |
| 35   | TC035   | Scrolling             | Verify Scroll Position After Pagination                    | P2       |
| 36   | TC036   | API Validation        | Verify Category Filter API Response Status is 200          | P0       |
| 37   | TC037   | API Validation        | Verify Search API Response Status is 200                   | P0       |
| 38   | TC038   | API Validation        | Verify Discovery Filter API Response Status is 200         | P0       |
| 39   | TC039   | API Validation        | Verify UI Movie Title Matches API Response                 | P0       |
| 40   | TC040   | API Validation        | Verify UI Movie Count Matches API Response                 | P0       |

