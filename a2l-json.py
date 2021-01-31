import sys
import json
import re

begin_project = '''/* @@@@ File written by CANAPE_VERSION 14 0 39 @@@@ */

ASAP2_VERSION 1 61
/begin PROJECT Example ""

  /begin MODULE CCP ""

    /begin A2ML


      struct Protocol_Layer {
        uint;  /* XCP protocol layer version, current 0x100*/
        uint;  /* T1 [ms] Time-out of the standard CTO, for example CONNECT*/
        uint;  /* T2 [ms] Time-out of the checksum calculation*/
        uint;  /* T3 [ms] Time-out of the non-volatile memory programming: PROGRAM_START, PROGRAM_VERIFY, PROGRAM_PREPARE*/
        uint;  /* T4 [ms] Time-out of the non-volatile memory programming: PROGRAM_CLEAR*/
        uint;  /* T5 [ms] Time-out of the non-volatile memory programming: PROGRAM, PROGRAM_RESET, PROGRAM_MAX*/
        uint;  /* T6 [ms] Time-out of the command CONNECT(USER_DEFINED)*/
        uint;  /* T7 [ms] Time-out of the pre-action*/
        uchar;  /* MAX_CTO: Indicates the maximum length of a CTO packet in bytes. */
        uint;  /* MAX_DTO: Indicates the maximum length of a DTO packet in bytes. */
        enum {
          "BYTE_ORDER_MSB_LAST" = 0,
          "BYTE_ORDER_MSB_FIRST" = 1
        };  /* BYTE_ORDER: BYTE_ORDER_MSB_LAST = Intel, BYTE_ORDER_MSB_FIRST = Motorola*/
        enum {
          "ADDRESS_GRANULARITY_BYTE" = 1,
          "ADDRESS_GRANULARITY_WORD" = 2,
          "ADDRESS_GRANULARITY_DWORD" = 4
        };  /*The address granularity indicates the size of an element contained at a single address.*/
        taggedstruct {
          ("OPTIONAL_CMD" enum {
            "GET_COMM_MODE_INFO" = 251,
            "GET_ID" = 250,
            "SET_REQUEST" = 249,
            "GET_SEED" = 248,
            "UNLOCK" = 247,
            "SET_MTA" = 246,
            "UPLOAD" = 245,
            "SHORT_UPLOAD" = 244,
            "BUILD_CHECKSUM" = 243,
            "TRANSPORT_LAYER_CMD" = 242,
            "USER_CMD" = 241,
            "DOWNLOAD" = 240,
            "DOWNLOAD_NEXT" = 239,
            "DOWNLOAD_MAX" = 238,
            "SHORT_DOWNLOAD" = 237,
            "MODIFY_BITS" = 236,
            "SET_CAL_PAGE" = 235,
            "GET_CAL_PAGE" = 234,
            "GET_PAG_PROCESSOR_INFO" = 233,
            "GET_SEGMENT_INFO" = 232,
            "GET_PAGE_INFO" = 231,
            "SET_SEGMENT_MODE" = 230,
            "GET_SEGMENT_MODE" = 229,
            "COPY_CAL_PAGE" = 228,
            "CLEAR_DAQ_LIST" = 227,
            "SET_DAQ_PTR" = 226,
            "WRITE_DAQ" = 225,
            "SET_DAQ_LIST_MODE" = 224,
            "GET_DAQ_LIST_MODE" = 223,
            "START_STOP_DAQ_LIST" = 222,
            "START_STOP_SYNCH" = 221,
            "GET_DAQ_CLOCK" = 220,
            "READ_DAQ" = 219,
            "GET_DAQ_PROCESSOR_INFO" = 218,
            "GET_DAQ_RESOLUTION_INFO" = 217,
            "GET_DAQ_LIST_INFO" = 216,
            "GET_DAQ_EVENT_INFO" = 215,
            "FREE_DAQ" = 214,
            "ALLOC_DAQ" = 213,
            "ALLOC_ODT" = 212,
            "ALLOC_ODT_ENTRY" = 211,
            "PROGRAM_START" = 210,
            "PROGRAM_CLEAR" = 209,
            "PROGRAM" = 208,
            "PROGRAM_RESET" = 207,
            "GET_PGM_PROCESSOR_INFO" = 206,
            "GET_SECTOR_INFO" = 205,
            "PROGRAM_PREPARE" = 204,
            "PROGRAM_FORMAT" = 203,
            "PROGRAM_NEXT" = 202,
            "PROGRAM_MAX" = 201,
            "PROGRAM_VERIFY" = 200
          })*;  /* XCP-Code of optional command supported by the slave*/
          "COMMUNICATION_MODE_SUPPORTED" taggedunion {
            "BLOCK" taggedstruct {
              "SLAVE" ;
              "MASTER" struct {
                uchar;  /* MAX_BS: Indicates the maximum allowed block size as the number of consecutive command packets in a block sequence*/
                uchar;  /* MIN_ST: Indicates the required minimum separation time between the packets of a block transfer from the master device to the slave device in units of 100 ms*/
              };
            };
            "INTERLEAVED" uchar;  /* QUEUE_SIZE: indicates the maximum number of consecutive command packets the master can send to the receipt queue of the slave*/
          };
          "SEED_AND_KEY_EXTERNAL_FUNCTION" char[256];  /* Name of the Seed&Key function*/
        };
      };

      struct Daq {
        enum {
          "STATIC" = 0,
          "DYNAMIC" = 1
        };  /*The flag indicates whether the DAQ lists that are not PREDEFINED shall be configured statically or dynamically*/
        uint;  /* MAX_DAQ: Total number of available DAQ lists */
        uint;  /* MAX_EVENT_CHANNEL: Total number of available event channels*/
        uchar;  /* MIN_DAQ: Total number of predefined DAQ lists */
        enum {
          "OPTIMISATION_TYPE_DEFAULT" = 0,
          "OPTIMISATION_TYPE_ODT_TYPE_16" = 1,
          "OPTIMISATION_TYPE_ODT_TYPE_32" = 2,
          "OPTIMISATION_TYPE_ODT_TYPE_64" = 3,
          "OPTIMISATION_TYPE_ODT_TYPE_ALIGNMENT" = 4,
          "OPTIMISATION_TYPE_MAX_ENTRY_SIZE" = 5
        };  /* Indicate the Type of Optimisation Method the master preferably should use.*/
        enum {
          "ADDRESS_EXTENSION_FREE" = 0,
          "ADDRESS_EXTENSION_ODT" = 1,
          "ADDRESS_EXTENSION_DAQ" = 3
        };  /*The flag indicates whether the address extension of all entries within one ODT or within one DAQ must be the same. */
        enum {
          "IDENTIFICATION_FIELD_TYPE_ABSOLUTE" = 0,
          "IDENTIFICATION_FIELD_TYPE_RELATIVE_BYTE" = 1,
          "IDENTIFICATION_FIELD_TYPE_RELATIVE_WORD" = 2,
          "IDENTIFICATION_FIELD_TYPE_RELATIVE_WORD_ALIGNED" = 3
        };  /* The type of Identification Field the slave will use when transferring DAQ Packets to the master*/
        enum {
          "GRANULARITY_ODT_ENTRY_SIZE_DAQ_BYTE" = 1,
          "GRANULARITY_ODT_ENTRY_SIZE_DAQ_WORD" = 2,
          "GRANULARITY_ODT_ENTRY_SIZE_DAQ_DWORD" = 4,
          "GRANULARITY_ODT_ENTRY_SIZE_DAQ_DLONG" = 8
        };  /* Granularity for size of ODT entry */
        uchar;  /* MAX_ODT_ENTRY_SIZE_DAQ Maximum size of ODT entry (DIRECTION = DAQ) */
        enum {
          "NO_OVERLOAD_INDICATION" = 0,
          "OVERLOAD_INDICATION_PID" = 1,
          "OVERLOAD_INDICATION_EVENT" = 2
        };  /*OVERLOAD_INDICATION_PID: This means the higest bit is set in the PID, when an overload occurs
OVERLOAD_INDICATION_EVENT: This means an event is set, when an overload occurs*/
        taggedstruct {
          "PRESCALER_SUPPORTED" ;  /*This flag indicates that all DAQ lists support the prescaler for reducing the transmission period.*/
          "RESUME_SUPPORTED" ;  /*This  flag indicates that all DAQ lists can be put in RESUME mode. */
          block "STIM" struct {
            enum {
              "GRANULARITY_ODT_ENTRY_SIZE_STIM_BYTE" = 1,
              "GRANULARITY_ODT_ENTRY_SIZE_STIM_WORD" = 2,
              "GRANULARITY_ODT_ENTRY_SIZE_STIM_DWORD" = 4,
              "GRANULARITY_ODT_ENTRY_SIZE_STIM_DLONG" = 8
            };  /* Granularity for size of ODT entry direction STIM*/
            uchar;  /* MAX_ODT_ENTRY_SIZE_STIM Maximum size of ODT entry (DIRECTION = STIM)*/
            taggedstruct {
              "BIT_STIM_SUPPORTED" ;  /*The flag indicates  whether  bitwise  data  stimulation  through BIT_OFFSET in WRITE_DAQ is supported.*/
            };
          };
          block "TIMESTAMP_SUPPORTED" struct {
            uint;  /*The timestamp will increment by TIMESTAMP_TICKS per unit and wrap around if an overflow occurs. */
            enum {
              "NO_TIME_STAMP" = 0,
              "SIZE_BYTE" = 1,
              "SIZE_WORD" = 2,
              "SIZE_DWORD" = 4
            };  /*Timestamp size in bytes*/
            enum {
              "UNIT_1NS" = 0,
              "UNIT_10NS" = 1,
              "UNIT_100NS" = 2,
              "UNIT_1US" = 3,
              "UNIT_10US" = 4,
              "UNIT_100US" = 5,
              "UNIT_1MS" = 6,
              "UNIT_10MS" = 7,
              "UNIT_100MS" = 8,
              "UNIT_1S" = 9
            };  /*Ticks per unit*/
            taggedstruct {
              "TIMESTAMP_FIXED" ;
            };  /* TIMESTAMP_FIXED flag indicates that the Slave always will send DTO Packets in time stamped mode. */
          };
          "PID_OFF_SUPPORTED" ;  /*Flag in DAQ_PROPERTIES indicates that transfer of DTO Packets without Identification Field is possible. */
          (block "DAQ_LIST" struct {
            uint;  /* DAQ_LIST_NUMBER  is in the range [0,1,..MIN_DAQ-1]. */
            taggedstruct {
              "DAQ_LIST_TYPE" enum {
                "DAQ" = 1,
                "STIM" = 2,
                "DAQ_STIM" = 3
              };  /* DAQ: DIRECTION = DAQ only 
 STIM: DIRECTION = STIM only 
 DAQ_STIM: both directions are possible */
              "MAX_ODT" uchar;  /*Number of ODTs in this DAQ list */
              "MAX_ODT_ENTRIES" uchar;  /*Maximum number of entries in an ODT*/
              "FIRST_PID" uchar;  /*FIRST_PID: Is the PID in the DTO Packet of the first ODT transferred by this DAQ list.*/
              "EVENT_FIXED" uint;  /*The flag indicates that the Event Channel for this DAQ list can not be changed. */
              block "PREDEFINED" taggedstruct {
                (block "ODT" struct {
                  uchar;  /* ODT number */
                  taggedstruct {
                    ("ODT_ENTRY" struct {
                      uchar;  /* ODT_ENTRY number */
                      ulong;  /* address of element */
                      uchar;  /* address extension of element */
                      uchar;  /* size of element [AG] */
                      uchar;  /* BIT_OFFSET */
                    })*;
                  };
                })*;
              };  /*PREDEFINED;The DAQ list is predefined and fixed in the slave devices memory.*/
            };
          })*;
          (block "EVENT" struct {
            char[101];  /* EVENT_CHANNEL_NAME */
            char[9];  /* EVENT_CHANNEL_SHORT_NAME */
            uint;  /* EVENT_CHANNEL_NUMBER*/
            enum {
              "DAQ" = 1,
              "STIM" = 2,
              "DAQ_STIM" = 3
            };  /* DAQ: only DAQ_LISTs with DIRECTION = DAQ 
 STIM: only DAQ_LISTs with DIRECTION = STIM 
 DAQ_STIM both kind of DAQ_LISTs*/
            uchar;  /* MAX_DAQ_LIST:Maximum number of DAQ lists in this event channel */
            uchar;  /* TIME_CYCLE: Event channel time cycle */
            uchar;  /* TIME_UNIT: Event channel time unit*/
            uchar;  /* PRIORITY:The event channel with event channel priority = FF has the highest priority */
          })*;
        };
      };

      taggedunion Daq_Event {
        "FIXED_EVENT_LIST" taggedstruct {
          ("EVENT" uint)*;
        };
        "VARIABLE" taggedstruct {
          block "AVAILABLE_EVENT_LIST" taggedstruct {
            ("EVENT" uint)*;
          };
          block "DEFAULT_EVENT_LIST" taggedstruct {
            ("EVENT" uint)*;
          };
        };
      };  /*This are characteristic for measurement objects*/

      struct Pag {
        uchar;  /* MAX_SEGMENTS: Is the total number of segments in the slave device*/
        taggedstruct {
          "FREEZE_SUPPORTED" ;  /*This flag indicates that all SEGMENTS can be put in FREEZE */
        };
      };

      struct Pgm {
        enum {
          "PGM_MODE_ABSOLUTE" = 1,
          "PGM_MODE_FUNCTIONAL" = 2,
          "PGM_MODE_ABSOLUTE_AND_FUNCTIONAL" = 3
        };  /*The  ABSOLUTE_MODE  and  FUNCTIONAL_MODE  flags  indicate  the  clear/programming mode that can be used */
        uchar;  /* MAX_SECTORS: Total number of available sectors */
        uchar;  /* MAX_CTO_PGM: Maximum CTO size for PGM */
        taggedstruct {
          (block "SECTOR" struct {
            char[101];  /* SECTOR_NAME */
            uchar;  /* SECTOR_NUMBER*/
            ulong;  /* Start address for this SECTOR */
            ulong;  /* Length of this SECTOR [AG] */
            uchar;  /* CLEAR_SEQUENCE_NUMBER: The Clear Sequence Number describe, in which subsequential order the master has to clear and program flash memory sectors.*/
            uchar;  /* PROGRAM_SEQUENCE_NUMBER: The Program Sequence Number describe, in which subsequential order the master has to clear and program flash memory sectors.*/
            uchar;  /* PROGRAM_METHOD: The work flow depends on mode  absolute access or functional access*/
          })*;
          "COMMUNICATION_MODE_SUPPORTED" taggedunion {
            "BLOCK" taggedstruct {
              "SLAVE" ;  /*This flag indicates whether the Slave Block Mode is available during Programming. */
              "MASTER" struct {
                uchar;  /* MAX_BS_PGM:MAX_BS: indicates the maximum allowed block size as the number of consecutive command packets in a block sequence*/
                uchar;  /* MIN_ST_PGM ndicates the required minimum separation time between the packets of a block transfer from the master device to the slave device in units of 100 ms*/
              };  /*This flag indicates whether the Master Block Mode is available */
            };
            "INTERLEAVED" uchar;  /* QUEUE_SIZE_PGM: This value describe the total count of bytes for this queue*/
          };
        };
      };

      struct Segment {
        uchar;  /* SEGMENT_NUMBER: Logical data segment number*/
        uchar;  /* Total number of available pages */
        uchar;  /* ADDRESS_EXTENSION: Address extension for this SEGMENT*/
        uchar;  /* COMPRESSION_METHOD: The COMPRESSION_x flags indicate which compression state of the incoming data the slave can process*/
        uchar;  /* ENCRYPTION_METHOD: The  ENCRYPTION_x flags indicate which encryption state of the incoming data the slave can process.*/
        taggedstruct {
          block "CHECKSUM" struct {
            enum {
              "XCP_ADD_11" = 1,
              "XCP_ADD_12" = 2,
              "XCP_ADD_14" = 3,
              "XCP_ADD_22" = 4,
              "XCP_ADD_24" = 5,
              "XCP_ADD_44" = 6,
              "XCP_CRC_16" = 7,
              "XCP_CRC_16_CITT" = 8,
              "XCP_CRC_32" = 9,
              "XCP_USER_DEFINED" = 255
            };  /* Checksum type*/
            taggedstruct {
              "MAX_BLOCK_SIZE" ulong;  /* Maximum block size for checksum calculation */
              "EXTERNAL_FUNCTION" char[256];  /* Name of the Checksum.DLL */
            };
          };
          (block "PAGE" struct {
            uchar;  /* PAGE_NUMBER: Logical page number*/
            enum {
              "ECU_ACCESS_NOT_ALLOWED" = 0,
              "ECU_ACCESS_ALLOWED_WITHOUT_XCP_ONLY" = 1,
              "ECU_ACCESS_ALLOWED_WITH_XCP_ONLY" = 2,
              "ECU_ACCESS_ALLOWED_DONT_CARE" = 3
            };  /*The ECU_ACCESS_x  flags indicate whether and how the ECU can access this page.*/
            enum {
              "XCP_READ_ACCESS_NOT_ALLOWED" = 0,
              "XCP_READ_ACCESS_ALLOWED_WITHOUT_ECU_ONLY" = 1,
              "XCP_READ_ACCESS_ALLOWED_WITH_ECU_ONLY" = 2,
              "XCP_READ_ACCESS_ALLOWED_DONT_CARE" = 3
            };  /*The XCP_x_ACCESS_y flags indicate whether and how the XCP master can access this page.*/
            enum {
              "XCP_WRITE_ACCESS_NOT_ALLOWED" = 0,
              "XCP_WRITE_ACCESS_ALLOWED_WITHOUT_ECU_ONLY" = 1,
              "XCP_WRITE_ACCESS_ALLOWED_WITH_ECU_ONLY" = 2,
              "XCP_WRITE_ACCESS_ALLOWED_DONT_CARE" = 3
            };  /*The XCP_WRITE_ACCESS_x flags indicate whether the  X CP master can write to this PAGE*/
            taggedstruct {
              "INIT_SEGMENT" uchar;  /* references segment that initialises this page */
            };
          })*;  /* PAGES for this SEGMENT */
          (block "ADDRESS_MAPPING" struct {
            ulong;  /* source address */
            ulong;  /* destination address */
            ulong;  /* length */
          })*;
          "PGM_VERIFY" ulong;  /* verification value for PGM */
        };
      };  /*Settings for MEMORY_SEGMENT */

      taggedstruct Common_Parameters {
        block "PROTOCOL_LAYER" struct Protocol_Layer;
        block "SEGMENT" struct Segment;
        block "DAQ" struct Daq;
        block "PAG" struct Pag;
        block "PGM" struct Pgm;
        block "DAQ_EVENT" taggedunion Daq_Event;
      };

      struct CAN_Parameters {
        uint;  /* XCP on CAN version, currentl 0x0100 */
        taggedstruct {
          "CAN_ID_BROADCAST" ulong;  /* Auto-detection CAN-ID */
          "CAN_ID_MASTER" ulong;  /* CMD/STIM CAN-ID */
          "CAN_ID_SLAVE" ulong;  /* RES/ERR/EV/SERV/DAQ CAN-ID */
          "BAUDRATE" ulong;  /* Baudrate in Hz */
          "SAMPLE_POINT" uchar;  /* Sample point in % of bit time */
          "SAMPLE_RATE" enum {
            "SINGLE" = 1,
            "TRIPLE" = 3
          };  /* Sample per bit */
          "BTL_CYCLES" uchar;  /* slots per bit time */
          "SJW" uchar;  /*Length synchr. segment */
          "SYNC_EDGE" enum {
            "SINGLE" = 1,
            "DUAL" = 2
          };  /* SINGLE: on falling edge only
 DUAL: on falling and rising edge*/
          "MAX_DLC_REQUIRED" ;  /* master to slave frames always to have DLC = MAX_DLC = 8*/
          (block "DAQ_LIST_CAN_ID" struct {
            uint;  /* reference to DAQ_LIST_NUMBER */
            taggedstruct {
              "VARIABLE" ;
              "FIXED" ulong;  /* this DAQ_LIST always on this CAN_ID */
            };  /* exclusive tags: either VARIABLE or FIXED */
          })*;
        };
      };

      struct SxI_Parameters {
        uint;  /* XCP on SxI version, currently 0x0100 */
        ulong;  /* BAUDRATE [Hz] */
        taggedstruct {
          "ASYNCH_FULL_DUPLEX_MODE" struct {
            enum {
              "PARITY_NONE" = 0,
              "PARITY_ODD" = 1,
              "PARITY_EVEN" = 2
            };  /* Parity bit settings*/
            enum {
              "ONE_STOP_BIT" = 1,
              "TWO_STOP_BITS" = 2
            };  /*Stop bit settings*/
          };
          "SYNCH_FULL_DUPLEX_MODE_BYTE" ;
          "SYNCH_FULL_DUPLEX_MODE_WORD" ;
          "SYNCH_FULL_DUPLEX_MODE_DWORD" ;
          "SYNCH_MASTER_SLAVE_MODE_BYTE" ;
          "SYNCH_MASTER_SLAVE_MODE_WORD" ;
          "SYNCH_MASTER_SLAVE_MODE_DWORD" ;
        };  /* exclusive tags */
        enum {
          "HEADER_LEN_BYTE" = 0,
          "HEADER_LEN_CTR_BYTE" = 1,
          "HEADER_LEN_WORD" = 2,
          "HEADER_LEN_CTR_WORD" = 3
        };  /* XCP packet header */
        enum {
          "NO_CHECKSUM" = 0,
          "CHECKSUM_BYTE" = 1,
          "CHECKSUM_WORD" = 2
        };  /* Checksum type*/
      };

      struct TCP_IP_Parameters {
        uint;  /* XCP on TCP_IP version, currently 0x0100 */
        uint;  /* PORT */
        taggedunion {
          "HOST_NAME" char[256];  /*Name of the host like localhost*/
          "ADDRESS" char[15];  /* IP address like 127.0.0.1*/
        };
      };

      struct UDP_IP_Parameters {
        uint;  /* XCP on UDP version, currently 0x0100 */
        uint;  /* PORT */
        taggedunion {
          "HOST_NAME" char[256];  /*Name of the host like localhost*/
          "ADDRESS" char[15];  /* IP address like 127.0.0.1*/
        };
      };

      struct ep_parameters {
        uchar;  /* ENDPOINT_NUMBER, not endpoint address */
        enum {
          "BULK_TRANSFER" = 2,
          "INTERRUPT_TRANSFER" = 3
        };
        uint;  /* wMaxPacketSize: Maximum packet  
 size of endpoint in bytes       */
        uchar;  /* bInterval: polling of endpoint  */
        enum {
          "MESSAGE_PACKING_SINGLE" = 0,
          "MESSAGE_PACKING_MULTIPLE" = 1,
          "MESSAGE_PACKING_STREAMING" = 2
        };  /* Packing of XCP Messages         
 SINGLE: Single per USB data packet    
 MULTIPLE: Multiple per USB data packet  
 STREAMING: No restriction by packet sizes*/
        enum {
          "ALIGNMENT_8_BIT" = 0,
          "ALIGNMENT_16_BIT" = 1,
          "ALIGNMENT_32_BIT" = 2,
          "ALIGNMENT_64_BIT" = 3
        };  /* Alignment mandatory for all packing types*/
        taggedstruct {
          "RECOMMENDED_HOST_BUFSIZE" uint;  /* Recommended size for the host 
 buffer size. The size is defined
 as multiple of wMaxPacketSize.  */
        };
      };

      struct USB_Parameters {
        uint;  /* XCP on USB version  
 e.g. "1.0" = 0x0100 */
        uint;  /* Vendor ID                       */
        uint;  /* Product ID                      */
        uchar;  /* Number of interface             */
        enum {
          "HEADER_LEN_BYTE" = 0,
          "HEADER_LEN_CTR_BYTE" = 1,
          "HEADER_LEN_FILL_BYTE" = 2,
          "HEADER_LEN_WORD" = 3,
          "HEADER_LEN_CTR_WORD" = 4,
          "HEADER_LEN_FILL_WORD" = 5
        };  /* XCP packet header */
        taggedunion {
          block "OUT_EP_CMD_STIM" struct ep_parameters;  /* OUT-EP for CMD and STIM (if not specified otherwise)*/
        };
        taggedunion {
          block "IN_EP_RESERR_DAQ_EVSERV" struct ep_parameters;  /* IN-EP for RES/ERR, 
 DAQ (if not specified otherwise) and  
 EV/SERV (if not specified otherwise)  */
        };
        taggedstruct {
          "ALTERNATE_SETTING_NO" uchar;  /* Number of alternate setting   */
          "INTERFACE_STRING_DESCRIPTOR" char[101];  /* String Descriptor of XCP interface*/
          (block "OUT_EP_ONLY_STIM" struct ep_parameters)*;  /* multiple OUT-EP's for STIM */
          (block "IN_EP_ONLY_DAQ" struct ep_parameters)*;  /* multiple IN-EP's for DAQ*/
          block "IN_EP_ONLY_EVSERV" struct ep_parameters;  /* only one IN-EP for EV/SERV*/
          (block "DAQ_LIST_USB_ENDPOINT" struct {
            uint;  /* reference to DAQ_LIST_NUMBER          */
            taggedstruct {
              "FIXED_IN" uchar;  /* this DAQ list always                
 ENDPOINT_NUMBER, not endpoint address */
              "FIXED_OUT" uchar;  /* this STIM list always               
 ENDPOINT_NUMBER, not endpoint address */
            };
          })*;
        };
      };

      enum packet_assignment_type {
        "NOT_ALLOWED" = 0,
        "FIXED" = 1,
        "VARIABLE_INITIALISED" = 2,
        "VARIABLE" = 3
      };

      struct buffer {
        uchar;  /* Buffer number*/
        taggedstruct {
          "MAX_FLX_LEN_BUF" taggedunion {
            "FIXED" uchar;  /* constant value, can't be modified on runtime */
            "VARIABLE" uchar;  /* initial value, can be modified on runtime*/
          };  /* maximal size of the buffer [byte]*/
          block "LPDU_ID" taggedstruct {
            "FLX_SLOT_ID" taggedunion {
              "FIXED" uint;  /* constant value, can't be modified on runtime*/
              "VARIABLE" taggedstruct {
                "INITIAL_VALUE" uint;
              };  /* initial value, can be modified on runtime*/
            };  /* FlexRay timing, slot id*/
            "OFFSET" taggedunion {
              "FIXED" uchar;  /* constant value, can't be modified on runtime*/
              "VARIABLE" taggedstruct {
                "INITIAL_VALUE" uchar;
              };  /* initial value, can be modified on runtime*/
            };  /* FlexRay timing, base cycle*/
            "CYCLE_REPETITION" taggedunion {
              "FIXED" uchar;  /* constant value, can't be modified on runtime*/
              "VARIABLE" taggedstruct {
                "INITIAL_VALUE" uchar;
              };  /* initial value, can be modified on runtime*/
            };  /* FlexRay timing, cycle repetition*/
            "CHANNEL" taggedunion {
              "FIXED" enum {
                "A" = 0,
                "B" = 1
              };  /* constant value, can't be modified on runtime*/
              "VARIABLE" taggedstruct {
                "INITIAL_VALUE" enum {
                  "A" = 0,
                  "B" = 1
                };
              };  /* initial value, can be modified on runtime*/
            };  /* FlexRay Channel A or B*/
          };  /* LPDU-ID,  Data  Link  Layer  Protocol  Data  Unit  Identifier*/
          block "XCP_PACKET" taggedstruct {
            "CMD" enum packet_assignment_type;
            "RES_ERR" enum packet_assignment_type;
            "EV_SERV" enum packet_assignment_type;
            "DAQ" enum packet_assignment_type;
            "STIM" enum packet_assignment_type;
          };  /* XCP packet type*/
        };
      };

      struct FLX_Parameters {
        uint;  /* XCP on FlexRay version
 e.g. "1.0" = 0x0100*/
        uint;  /* T1_FLX [ms] Time-out while waiting for an XCP on FlexRay response
 e.g. FLX_ASSIGN*/
        char[256];  /* FIBEX-file with extension and without path, including CHI information*/
        char[256];  /* cluster-ID, id attribute of the FIBEX cluster*/
        uchar;  /* NAX, node address of the ECU*/
        enum {
          "HEADER_NAX" = 0,
          "HEADER_NAX_FILL" = 1,
          "HEADER_NAX_CTR" = 2,
          "HEADER_NAX_FILL3" = 3,
          "HEADER_NAX_CTR_FILL2" = 4,
          "HEADER_NAX_LEN" = 5,
          "HEADER_NAX_CTR_LEN" = 6,
          "HEADER_NAX_FILL2_LEN" = 7,
          "HEADER_NAX_CTR_FILL_LEN" = 8
        };  /* header type of the XCP on FlexRay message*/
        enum {
          "PACKET_ALIGNMENT_8" = 0,
          "PACKET_ALIGNMENT_16" = 1,
          "PACKET_ALIGNMENT_32" = 2
        };  /* XCP packet alignment within the XCP on FlexRay Message*/
        taggedunion {
          block "INITIAL_CMD_BUFFER" struct buffer;
        };  /* XCP dedicated buffer used to transmit XCP commands*/
        taggedunion {
          block "INITIAL_RES_ERR_BUFFER" struct buffer;
        };  /* XCP dedicated buffer used to receive the responses on the XCP commands*/
        taggedstruct {
          (block "POOL_BUFFER" struct buffer)*;
        };  /* XCP dedicated buffer(s) used for XCP-DAQ, -STIM and -EV/SERV*/
      };

      block "IF_DATA" taggedunion if_data {

        "CANAPE_EXT" struct {
          int;             /* version number */
          taggedstruct {
            "LINK_MAP" struct {
              char[256];   /* segment name */
              long;        /* base address of the segment */
              uint;        /* address extension of the segment */
              uint;        /* flag: address is relative to DS */
              long;        /* offset of the segment address */
              uint;        /* datatypValid */
              uint;        /* enum datatyp */
              uint;        /* bit offset of the segment */
            };
            "DISPLAY" struct {
              long;        /* display color */
              double;      /* minimal display value (phys)*/
              double;      /* maximal display value (phys)*/
            };
            "VIRTUAL_CONVERSION" struct {
              char[256];   /* name of the conversion formula */
            };
          };
        };
        "CANAPE_MODULE" struct {
          taggedstruct {
            ("RECORD_LAYOUT_STEPSIZE" struct {
              char[256];   /* name of record layout*/
              uint;        /* stepsize for FNC_VALUES */
              uint;        /* stepsize for AXIS_PTS_X */
              uint;        /* stepsize for AXIS_PTS_Y */
              uint;        /* stepsize for AXIS_PTS_Z */
              uint;        /* stepsize for AXIS_PTS_4 */
              uint;        /* stepsize for AXIS_PTS_5 */
            })*;
          };
        };
        "CANAPE_ADDRESS_UPDATE" taggedstruct {
          ("EPK_ADDRESS" struct {
            char[1024];         /* name of the corresponding symbol in MAP file */
            long;               /* optional address offset */
          })*;
          "ECU_CALIBRATION_OFFSET" struct {
            char[1024];         /* name of the corresponding symbol in MAP file */
            long;               /* optional address offset */
          };
          (block "CALIBRATION_METHOD" taggedunion {
            "AUTOSAR_SINGLE_POINTERED" struct {
              char[1024];         /* MAP symbol name for pointer table in RAM */
              long;               /* optional address offset */
              taggedstruct {
                "ORIGINAL_POINTER_TABLE" struct {
                  char[1024];    /* MAP symbol name for pointer table in FLASH */
                  long;          /* optional address offset */
                };
              };
            };
            "InCircuit2" struct {
              char[1024];         /* MAP symbol name for pointer table in RAM */
              long;               /* optional address offset */
              taggedstruct {
                "ORIGINAL_POINTER_TABLE" struct {
                  char[1024];    /* MAP symbol name for pointer table in FLASH */
                  long;          /* optional address offset */
                };
                "FLASH_SECTION" struct {
                  ulong;       /* start address of flash section */
                  ulong;       /* length of flash section */
                };
              };
            };
          })*;
          block "MAP_SYMBOL" taggedstruct {
            "FIRST" struct {
              char[1024];  /* symbol name of the corresponding segment in MAP file */
              long;        /* offset */
            };
            "LAST" struct {
              char[1024];  /* symbol name of the corresponding segment in MAP file */
              long;        /* offset */
            };
            ("ADDRESS_MAPPING_XCP" struct {
              char[1024];  /* symbol name of source range in MAP file */
              char[1024];  /* symbol name of destination range in MAP file */
            })*;
          };
          (block "MEMORY_SEGMENT" struct {
            char[1024];         /* name of the memory segment */
            taggedstruct {
              "FIRST" struct {
                char[1024];  /* symbol name of the corresponding segment in MAP file */
                long;        /* offset */
              };
              "LAST" struct {
                char[1024];  /* symbol name of the corresponding segment in MAP file */
                long;        /* offset */
              };
              ("ADDRESS_MAPPING_XCP" struct {
                char[1024];  /* symbol name of source range in MAP file */
                char[1024];  /* symbol name of destination range in MAP file */
              })*;
            };
          })*;
        };
        "CANAPE_GROUP" taggedstruct {
          block "STRUCTURE_LIST" (char[1024])*;
        };

        "XCP" struct {
          taggedstruct Common_Parameters;  /* default parameters */
          taggedstruct {
            block "XCP_ON_CAN" struct {
              struct CAN_Parameters;  /* specific for CAN */
              taggedstruct Common_Parameters;  /* overruling of default */
            };
            block "XCP_ON_SxI" struct {
              struct SxI_Parameters;  /* specific for SxI */
              taggedstruct Common_Parameters;  /* overruling of default */
            };
            block "XCP_ON_TCP_IP" struct {
              struct TCP_IP_Parameters;  /* specific for TCP_IP */
              taggedstruct Common_Parameters;  /* overruling of default */
            };
            block "XCP_ON_UDP_IP" struct {
              struct UDP_IP_Parameters;  /* specific for UDP_IP   */
              taggedstruct Common_Parameters;  /* overruling of default */
            };
            block "XCP_ON_USB" struct {
              struct USB_Parameters;  /* specific for USB      */
              taggedstruct Common_Parameters;  /* overruling of default */
            };
            block "XCP_ON_FLX" struct {
              struct FLX_Parameters;  /* specific for FlexRay  */
              taggedstruct Common_Parameters;  /* overruling of default */
            };
          };  /* transport layer parameters*/
        };
      };

    /end A2ML

    /begin MOD_COMMON ""
      BYTE_ORDER MSB_LAST
      ALIGNMENT_BYTE 1
      ALIGNMENT_WORD 1
      ALIGNMENT_LONG 1
      ALIGNMENT_INT64 1
      ALIGNMENT_FLOAT32_IEEE 1
      ALIGNMENT_FLOAT64_IEEE 1
    /end MOD_COMMON

    /begin IF_DATA XCP
      /begin PROTOCOL_LAYER
        0x0100
        0x07D0
        0x2710
        0x00
        0x00
        0x00
        0x00
        0x00
        0x08
        0x08
        BYTE_ORDER_MSB_LAST
        ADDRESS_GRANULARITY_BYTE
        OPTIONAL_CMD ALLOC_ODT_ENTRY
        OPTIONAL_CMD ALLOC_ODT
        OPTIONAL_CMD ALLOC_DAQ
        OPTIONAL_CMD FREE_DAQ
        OPTIONAL_CMD GET_DAQ_EVENT_INFO
        OPTIONAL_CMD GET_DAQ_RESOLUTION_INFO
        OPTIONAL_CMD GET_DAQ_PROCESSOR_INFO
        OPTIONAL_CMD START_STOP_SYNCH
        OPTIONAL_CMD START_STOP_DAQ_LIST
        OPTIONAL_CMD GET_DAQ_LIST_MODE
        OPTIONAL_CMD SET_DAQ_LIST_MODE
        OPTIONAL_CMD WRITE_DAQ
        OPTIONAL_CMD SET_DAQ_PTR
        OPTIONAL_CMD CLEAR_DAQ_LIST
        OPTIONAL_CMD DOWNLOAD
        OPTIONAL_CMD SHORT_UPLOAD
        OPTIONAL_CMD UPLOAD
        OPTIONAL_CMD SET_MTA
        OPTIONAL_CMD GET_COMM_MODE_INFO
      /end PROTOCOL_LAYER
      /begin DAQ
        DYNAMIC
        0x00
        0x03
        0x00
        OPTIMISATION_TYPE_DEFAULT
        ADDRESS_EXTENSION_FREE
        IDENTIFICATION_FIELD_TYPE_ABSOLUTE
        GRANULARITY_ODT_ENTRY_SIZE_DAQ_BYTE
        0x07
        OVERLOAD_INDICATION_PID
        PRESCALER_SUPPORTED
        /begin EVENT
          "XcpEvent_5msCycle"
          "XcpEvent_"
          0x00
          DAQ
          0x01
          0x05
          0x06
          0x00
        /end EVENT
        /begin EVENT
          "XcpEvent_2msCycle"
          "XcpEvent_"
          0x01
          DAQ
          0x01
          0x02
          0x06
          0x00
        /end EVENT
        /begin EVENT
          "XcpEvent_10msCycle"
          "XcpEvent_"
          0x02
          DAQ
          0x01
          0x0A
          0x06
          0x00
        /end EVENT
      /end DAQ
      /begin PAG
        0x00
      /end PAG
      /begin PGM
        PGM_MODE_ABSOLUTE
        0x00
        0x00
      /end PGM
      /begin XCP_ON_CAN
        0x0100
        CAN_ID_MASTER 0x0681
        CAN_ID_SLAVE 0x0686
        BAUDRATE 0x07A120
        SAMPLE_POINT 0x4B
        SAMPLE_RATE SINGLE
        BTL_CYCLES 0x08
        SJW 0x02
        SYNC_EDGE SINGLE
      /end XCP_ON_CAN
    /end IF_DATA
    /begin IF_DATA CANAPE_ADDRESS_UPDATE
    /end IF_DATA

    /begin MOD_PAR ""
    /end MOD_PAR\n\n\n\n'''
end_project = '''
    /begin RECORD_LAYOUT __UBYTE_Z 
      FNC_VALUES 1 UBYTE ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __UWORD_Z 
      FNC_VALUES 1 UWORD ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __ULONG_Z 
      FNC_VALUES 1 ULONG ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __SBYTE_Z 
      FNC_VALUES 1 SBYTE ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __SWORD_Z 
      FNC_VALUES 1 SWORD ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __SLONG_Z 
      FNC_VALUES 1 SLONG ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __FLOAT32_IEEE_Z 
      FNC_VALUES 1 FLOAT32_IEEE ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __FLOAT64_IEEE_Z 
      FNC_VALUES 1 FLOAT64_IEEE ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __UBYTE_S 
      FNC_VALUES 1 UBYTE COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __UWORD_S 
      FNC_VALUES 1 UWORD COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __ULONG_S 
      FNC_VALUES 1 ULONG COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __SBYTE_S 
      FNC_VALUES 1 SBYTE COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __SWORD_S 
      FNC_VALUES 1 SWORD COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __SLONG_S 
      FNC_VALUES 1 SLONG COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __FLOAT32_IEEE_S 
      FNC_VALUES 1 FLOAT32_IEEE COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __FLOAT64_IEEE_S 
      FNC_VALUES 1 FLOAT64_IEEE COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__UBYTE_S 
      AXIS_PTS_X 1 UBYTE INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__UWORD_S 
      AXIS_PTS_X 1 UWORD INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__ULONG_S 
      AXIS_PTS_X 1 ULONG INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__SBYTE_S 
      AXIS_PTS_X 1 SBYTE INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__SWORD_S 
      AXIS_PTS_X 1 SWORD INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__SLONG_S 
      AXIS_PTS_X 1 SLONG INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__FLOAT32_IEEE_S 
      AXIS_PTS_X 1 FLOAT32_IEEE INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__FLOAT64_IEEE_S 
      AXIS_PTS_X 1 FLOAT64_IEEE INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __A_UINT64_Z 
      FNC_VALUES 1 A_UINT64 ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __A_INT64_Z 
      FNC_VALUES 1 A_INT64 ROW_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __A_UINT64_S 
      FNC_VALUES 1 A_UINT64 COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT __A_INT64_S 
      FNC_VALUES 1 A_INT64 COLUMN_DIR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__A_UINT64_S 
      AXIS_PTS_X 1 A_UINT64 INDEX_INCR DIRECT
    /end RECORD_LAYOUT

    /begin RECORD_LAYOUT SSV__A_INT64_S 
      AXIS_PTS_X 1 A_INT64 INDEX_INCR DIRECT
    /end RECORD_LAYOUT

  /end MODULE
/end PROJECT
'''

map_template = '''    /begin CHARACTERISTIC {var_name} ""
      MAP 0x7000AFA0 __{var_type}_Z 0 {compu_method}  {var_range}
      ECU_ADDRESS_EXTENSION 0x0
      EXTENDED_LIMITS {var_range}
{sub_axis}      /begin IF_DATA CANAPE_EXT
        100
        LINK_MAP "{var_name}{var_map}" {var_addr} 0 0 0 0 0 0
        DISPLAY 0 {display_range}
      /end IF_DATA
      SYMBOL_LINK "{var_name}{var_map}" 0
      FORMAT "%.15"
    /end CHARACTERISTIC\n\n'''



axis_subtemplate = '''      /begin AXIS_DESCR
        FIX_AXIS NO_INPUT_QUANTITY {compu_method}  {axis} {var_range}
        EXTENDED_LIMITS {var_range}
        DEPOSIT ABSOLUTE
        FORMAT "%.15"
        FIX_AXIS_PAR_DIST 0 1 {axis}
      /end AXIS_DESCR\n'''

s_axis_subtemplate = '''      /begin AXIS_DESCR
        COM_AXIS NO_INPUT_QUANTITY {compu_method}  {axis} {var_range}
        EXTENDED_LIMITS {var_range}
        DEPOSIT ABSOLUTE
        FORMAT "%.15"
        AXIS_PTS_REF {var_name}
      /end AXIS_DESCR\n'''

s_axis_template = '''    /begin AXIS_PTS {var_name} ""
      {var_addr} NO_INPUT_QUANTITY SSV__{var_type}_S 0 {compu_method} {axis} {display_range}
      ECU_ADDRESS_EXTENSION 0x0
      EXTENDED_LIMITS {var_range}
      DEPOSIT ABSOLUTE
      /begin IF_DATA CANAPE_EXT
        100
        LINK_MAP "{var_name}{var_map}" {var_addr} 0 0 0 0 0 0
        DISPLAY 0 {display_range}
      /end IF_DATA
      SYMBOL_LINK "{var_name}{var_map}" 0
      FORMAT "%.15"
    /end AXIS_PTS\n\n'''


measure_template = '''    /begin MEASUREMENT {var_name} ""
      {var_type} {compu_method} 0 0 {var_range}
      READ_WRITE
      ECU_ADDRESS {var_addr}
      ECU_ADDRESS_EXTENSION 0x0
      FORMAT "%.15"
{matrix}{layout}      /begin IF_DATA CANAPE_EXT
        100
        LINK_MAP "{var_name}{var_map}" {var_addr} 0 0 0 0 0 0
        DISPLAY 0 {display_range}
      /end IF_DATA
      SYMBOL_LINK "{var_name}{var_map}" 0
    /end MEASUREMENT\n\n'''

conv_template = '''    /begin COMPU_METHOD {var_name}.CONVERSION "@@@@RuleName created by CANape"
      LINEAR "%3.1" ""
      COEFFS_LINEAR {conv} 0
    /end COMPU_METHOD\n\n'''

item_template = '''{indent}/begin {ID} {ID_NAME} {comment}
{contents}{indent}/end {ID}\n'''
    
def read_jsonc(fname):
    with open(fname, 'r') as f:
        try:
            return json.loads(re.sub("//.*","",f.read(),flags=re.M))
        except:
            print('Invalid json format : {0}'.format(fname))
            sys.exit(1)

def read_file(fname):
    with open (fname, 'r') as f:
        return f.read()
        
class AsapJson:
    def __init__(self, map_fname=''):
        if map_fname:
            self.mapdata = read_file(map_fname)
    def from_json(self, json_fname):
        dic_con = read_jsonc(json_fname)

        self.dic_var = dic_con['variable']

        # map : put last to the map caused shared axis
        self.list_sorted_var = [d for d in self.dic_var 
                if not 'A2L_TYPE' in self.dic_var[d] 
                or self.dic_var[d]['A2L_TYPE'] != 'MAP']
        self.list_sorted_var += [d for d in self.dic_var 
                if 'A2L_TYPE' in self.dic_var[d] 
                and self.dic_var[d]['A2L_TYPE'] == 'MAP']

        self.dic_type = dic_con['type']
        self.dic_size = dic_con['type_size']
        self.dic_range = dic_con['type_range']

    def update_a2l(self):
        if not hasattr(self, 'mapdata'):
            print("load your map file first")
            sys.exit(1)

        var_name = 'Rte_APP_SFA_SD_PiVehTuneParameterInfo_DeBoostCurve'
        m = re.search(r'{0}\s+\|\s+0x([0-9a-fA-F]{{8}})'.format(var_name), self.mapdata)
        if m:
            var_addr = '0x{0}'.format(m.group(1).upper())
            print(var_addr)

    def to_a2l(self, a2l_fname):
        def apply_axis_template(axis, sub_axis):
            _template = sub_axis
            for a in ['x','y','z']:
                if axis[a] > 1:
                        _template[a] = axis_subtemplate.format(
                            var_range=var_range,
                            compu_method='NO_COMPU_METHOD',
                            axis=axis[a])
                if 'shared_axis' in v:
                    print(v)
                    if a in v['shared_axis']:
                        if v['shared_axis'][a] in dic_shared_axis:
                            shared_a = dic_shared_axis[v['shared_axis'][a]]
                            _template[a] = s_axis_subtemplate.format(
                                var_name=v['shared_axis'][a],
                                var_range=shared_a['var_range'],
                                compu_method=shared_a['compu_method'],
                                axis=axis[a]
                    )
            return _template
        
        def apply_array(text_array):
            m = re.search(r'(\[(?P<x>\d+)\])(\[(?P<y>\d+)\])?(\[(?P<z>\d+)\])?', text_array)
            if m:
                axis = {}
                axis['x'] = int(m.group('x')) if m.group('x') else 1
                axis['y'] = int(m.group('y')) if m.group('y') else 1
                axis['z'] = int(m.group('z')) if m.group('z') else 1
                matrix = '      MATRIX_DIM {0} {1} {2}\n'\
                        .format(axis['x'], axis['y'], axis['z'])
                layout = '      LAYOUT ROW_DIR\n'

                var_map = ''
                if axis['x'] > 1:
                    var_map += '._0_'
                if axis['y'] > 1:
                    var_map += '._0_'
                if axis['z'] > 1:
                    var_map += '._0_'
            return matrix, layout, var_map, axis
        
        def apply_conv(vname, v):
            if 'conv' in v:
                return vname+'.CONVERSION'
            else:
                return 'NO_COMPU_METHOD'
        dic_shared_axis = {}
        measure_texts = ''
        conv_texts = ''
        def set_contents_from_list(key, dictionary, indent=4):
            if key in dictionary:
                return item_template.format(
                            indent=' '*indent,
                            ID=key,
                            ID_NAME='',
                            comment='',
                            contents=set_contents(dictionary[key], indent+2))
            else:
                return ''

        def set_template_item(item, key, contents, indent=4):
            return item_template.format(
                    indent=' '*indent,
                    ID=item,
                    ID_NAME=key,
                    comment='""',
                    contents=contents) + '\n'

        def set_contents(list_item, indent=4):
            return ''.join(['{s}{0}\n'.format(d, s=' '*indent) for d in list_item])
        def set_content(text, indent=6):
            return '{s}{0}\n'.format(text, s=' '*indent)
        def set_link_map(text, indent=6):
            return '{s}/begin IF_DATA CANAPE_EXT\n{s2}100\n{s2}LINK_MAP "{0}" 0 0 0 0 0 0 0\n{s}/end IF_DATA\n'.format(
                    text, s=' '*indent, s2=' '*(indent+2))
        def append_value(dict_obj, key, value):
                if key not in dict_obj:
                    dict_obj[key] = [value]
                else:
                    dict_obj[key].append(value)

        dic_g = {}
        for vname in self.list_sorted_var:
            v = self.dic_var[vname]
            if 'array' in v:
                matrix, layout, var_map, axis = apply_array(v['array'])
            else:
                matrix, layout, var_map, axis = '', '', '', {'x':'','y':'','z':''}

            var_addr = '0x0'
            if hasattr(self, 'mapdata'):
                m = re.search(r'{0}\s+(0x[0-9a-fA-F]{{8}})'.format(v['name']), self.mapdata)
                if m:
                    var_addr = m.group(1)
            sub_axis = {'x':'','y':'','z':''}
            compu_method = apply_conv(vname, v)
            var_range = self.dic_range[v['type']]
            var_type = self.dic_type[v['type']]

            if 'A2L_TYPE' in v:
                if v['A2L_TYPE'] == 'shared_axis':
                    template = s_axis_template
                    dic_shared_axis[vname] = {
                            'var_range':var_range,
                            'compu_method':compu_method,
                            }
                elif v['A2L_TYPE'] == 'map':
                    template = map_template
                    sub_axis = apply_axis_template(axis, sub_axis)
                elif v['A2L_TYPE'] == 'STRING':
                    contents = set_content('ASCII {var_addr} __{var_type}_Z 0 NO_COMPU_METHOD 0 255'.format(
                        var_addr=var_addr,
                        var_type=var_type))
                    contents += set_content('NUMBER {0}'.format(x))
                    contents += set_link_map(vname)
                    measure_text = set_template_item('CHARACTERISTIC', vname, contents)
                elif v['A2L_TYPE'] == 'MAP':
                    contents = set_content('MAP 0 RL_{0} 0 NO_COMPU_METHOD 0 255'.format(var_type))
                    contents += set_content('NUMBER {0}'.format(x))
                    contents += set_link_map(vname)
                    measure_text = set_template_item('CHARACTERISTIC', vname, contents)

            else:
                # text = measure_template.format(
                #     var_name=var_name,
                #     var_type=var_type,
                #     array=array,
                #     var_addr=var_addr,
                #     _0_=_0_
                # )
                template = measure_template
                measure_text = template.format(
                var_name=vname,
                var_type=self.dic_type[v['type']],
                matrix=matrix,
                layout=layout,
                var_addr=var_addr,
                var_map=var_map,
                var_range=var_range,
                display_range=var_range,
                axis=axis['x'],
                compu_method=compu_method,
                sub_axis=''.join(sub_axis.values()))

            if 'conv' in v:
                conv_texts += conv_template.format(
                var_name=vname,
                conv=v['conv'])

            if 'group' in v:
                root_group, list_sub_group = v['group'].split('/')[0], v['group'].split('/')
                
                # GROUP
                if root_group not in dic_g:
                    dic_g[root_group] = {'type' : 'GROUP'}

                # SUB_GROUP
                for idx, val in enumerate(list_sub_group):
                    if val not in dic_g:
                        dic_g[val] = {'type' : 'SUB_GROUP'}
                    if idx+1 < len(list_sub_group):
                        append_value(dic_g[val], 'SUB_GROUP', list_sub_group[idx+1])
                # variable
                if 'A2L_TYPE' in v:
                    append_value(dic_g[list_sub_group[-1]], 'REF_MEASUREMENT', vname)
                else:
                    append_value(dic_g[list_sub_group[-1]], 'REF_CHARACTERISTIC', vname)

        group_text = ''
        for key in dic_g:
            contents = ''
            if dic_g[key]['type'] == 'GROUP':
                contents = set_content('ROOT')
            
            for con_list in ['SUB_GROUP','FUNCTION_LIST','REF_CHARACTERISTIC','REF_MEASUREMENT']:
                contents += set_contents_from_list(con_list, dic_g[key], indent=6)

            group_text += set_template_item('GROUP', key, contents)

        a2l_text = begin_project + conv_texts + measure_texts + end_project

        with open(a2l_fname, 'w') as f:
            f.write(a2l_text)

if __name__=='__main__':
    aj = AsapJson()
    aj.from_json('variable2.json')
    aj.to_a2l('template.a2l')
